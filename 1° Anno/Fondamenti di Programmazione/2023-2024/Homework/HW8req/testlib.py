import time, sys
import importlib
import stopit
import unittest, unittest.mock
from hashlib import sha1
from contextlib import contextmanager
import tempfile, os, os.path
#from icontract import require, ensure

DEBUG=True
DEBUG=False

class UnderstandingError(Exception): pass   # errore nelle domande di comprensione del testo
class ForbiddenError(Exception):     pass   # errore nell'import o nell'aprire un file proibito
class TimeoutError(Exception):       pass   # errore di timeout


class TestCase(unittest.TestCase):
    FEEDBACKS = {}                              # feedbacks for text comprehension questions
    __orig_import = __builtins__['__import__']
    __orig_open   = __builtins__['open']
    __orig_print  = __builtins__['print']
    __skipSome    = False                       # if True some tests are skipped during timing

    def _raise_forbidden(self, forbidden):
        # Lamdable method that throws an exception
        raise ForbiddenError(f"The usage of the '{forbidden}' function/method is forbidden!")

    def forbidden_function(self, target='os.walk'):
        # Return a 'with' context to forbid using a target function: by default 'os.walk'
        return unittest.mock.patch(target, new=lambda *x, **k: self._raise_forbidden( target ))

    def check_imports(self, allowed=None, forbidden=None):
        if allowed   is None: allowed   = []
        if forbidden is None: forbidden = []
        # Return a 'with' context to forbid imports not listed in 'allowed' or listed in 'forbidden'
        def _check_import(*args, **kargs):
            name, *rest = args
            if name in forbidden or (not forbidden and name not in allowed):
                print(f"Importing {name} (globals, locals, {rest[-2:]}) (not allowed)")
                raise ForbiddenError(f"The import of '{name}' is forbidden")
            else:
                return self.__orig_import(*args, **kargs)
        return unittest.mock.patch('builtins.__import__', new=_check_import)

    def check_open(self, allowed=None):
        'allows opening only the allowed filenames with the given modes'
        if not allowed:   allowed   = {}
        def _check_open(*args, **kargs):
            if len(args) > 1:
                mode = args[1]
            else:
                mode = kargs.get('mode', 'r')
            filename = args[0]
            while '//' in filename:
                filename = filename.replace('//','/')
            for fn,m in allowed.items():
                #print(f"Checking file '{filename}' with mode '{mode}' ('{fn}':'{m}')")
                if filename.endswith(fn):
                    if not mode in m:
                        #print(f"Opening file '{filename}' with mode '{mode}' is not allowed!")
                        raise ForbiddenError(f"Opening file '{filename}' with mode='{mode}' is forbidden!")
                    else:
                        # found and allowed
                        break
            else: # not found and not allowed
                #print(f"Opening file '{filename}' is not allowed!")
                raise ForbiddenError(f"Opening file '{filename}' is forbidden!")
            # print(f"Opening file {filename} with mode {mode} (allowed)")
            return self.__orig_open(*args, **kargs)
        return unittest.mock.patch('builtins.open', new=_check_open)

    def ignore_print(self):
        "ignore all printing except when it's to a file"
        def _check_print(*args, **kargs):
            if 'file' in kargs:
                #self.__orig_print('printing in file', kargs['file'].name, args)
                self.__orig_print(*args, **kargs)
        return unittest.mock.patch('builtins.print', new=_check_print)

    def ignored_function(self, target='builtins.print'):
        # Return a 'with' context that ignores a target function: by default 'builtins.print'
        return unittest.mock.patch(target, new=lambda *x, **k: None)

    def check_comprehension_questions(self, answers=None, corrects=None):
        "test sulla comprensione del testo a partire dall'elenco di domande/feedback e delle risposte di docente e studente"
        __tracebackhide__ = True
        for question, feedbacks in self.FEEDBACKS.items():
            answer = None if answers  is None else answers.get(question, None)
            if answer is None:
                raise UnderstandingError(f"Non hai risposto alla domanda '{question}'")
            if isinstance(answer, str): answer = answer.lower()
            correct = None if corrects is None else corrects.get(question, None)
            if correct is None:
                raise UnderstandingError(f"TESTERROR: il docente non ha indicato la risposta giusta alla domanda '{question}'")
            for answers, feedback in feedbacks.items():
                if answer in answers:
                    break
            else:
                raise UnderstandingError(f"Non capisco la tua risposta '{answer}' alla domanda '{question}'")
            if correct in answers:
                print(f"""
Alla domanda '{question}'
hai risposto '{answer}'.
Bene! {feedback}""")
            else:
                raise UnderstandingError(f"""Alla domanda: '{question}'
hai risposto '{answer}'.
Peccato! {feedback}""")

    @contextmanager
    def timer(self, timeout):
        '''Return a context in which the execution time is measured and, if necessary, a time-out exception is thrown.
        This way, the timeout is detected even if the timeout signal is captured. (yield version)'''
        start = time.time()
        try:
            yield start
        finally:
            wallclock_time = round(time.time() - start, 3)
            if wallclock_time > timeout:
                raise TimeoutError(f'Timeout! ({wallclock_time} > {timeout})')

    def timeout(self, sec):
        '''Return a 'with' context to stop the code when the timeout expires.'''
        return stopit.ThreadingTimeout(sec, swallow_exc=False)
        #return stopit.SignalTimeout(sec, swallow_exc=False)

    def print_timing(self, G, args, T=5, N=10, M=5):
        '''Per M volte si misura il tempo necessario per eseguire N esecuzioni (reference e implementation).
            Di queste M si prendono le due minori e se ne calcola il rapporto'''
        from timeit import timeit
        ref    = timeit('reference' + args, number=N, globals=G)
        X      = round(T/ref)               # X tale da metterci almeno T secondi
        X      = max(X, 10)                 # con un minimo di N volte
        imple  = min(timeit('implementation' + args, number=X, globals=G) for _ in range(M))    # min time over M run
        ref    = min(timeit('reference'      + args, number=X, globals=G) for _ in range(M))    # min time over M run
        ratio  = imple/ref
        print(  f"{X} runs executed, reference time: {ref:0.3}s, your time: {imple:0.3}s, speed ratio: {ratio:0.2} times",
                'slower' if ratio > 0 else 'faster', "than the reference implementation")

    def check_max_ciclomatic_complexity(_self, file='program01.py', level=10):
        'raise an exception if the max cyclomatic complexity of the file is above the level'
        from radon.complexity   import cc_visit, cc_rank, sorted_results
        __tracebackhide__ = True
        with open(file, encoding='utf8') as F:
            text = F.read()
        worst = sorted_results(cc_visit(text))[0]  # FIXME: we assume at least one function is there
        cc = worst.complexity
        rank = cc_rank(cc)
        desired = cc_rank(level)
        fun = worst.name
        # TODO: elencare TUTTE le funzioni con cc alta invece che solo la massima?
        _self.assertLessEqual(cc, level, f"""
Your function/method '{fun}' has maximum cyclomatic complexity {cc} ({rank}), 
which is bigger than the minimum allowed {level} ({desired}).
Please implement your algorithm by using smaller functions/methods.""")


    @contextmanager
    def assertIsRecursive(self, module):
        '''Return a 'with' context to check for recursion.'''
        import isrecursive
        with    self.imported(module) as program01, \
                self.decorated(program01) as program, \
                self.assertRaises( isrecursive.RecursionDetectedError ):
            yield program

    @contextmanager
    def decorated(self, module):
        '''Return a 'with' context decorating all functions/methods to raise RecursionDetectedError if recursive.'''
        import isrecursive
        isrecursive.decorate_module(module)
        try:
            yield module
        finally:
            isrecursive.undecorate_module(module)
        
    @contextmanager
    def imported(self, module):
        '''Return a 'with' context to import/unimport the module'''
        program = importlib.import_module(module)
        try:
            yield program
        finally:
            del program
            del sys.modules[module]

    @contextmanager
    def randomized_symbol(self, module, symbol):
        '''Renames randomly a symbol in a module'''
        import random, string
        random_name = ''.join(random.choices(string.ascii_letters, k=20))
        if DEBUG: print(module, symbol, ' -> ', random_name)
        value = getattr(module, symbol)
        setattr(module, random_name, value)
        delattr(module, symbol)
        try:
            yield random_name
        finally:
            if DEBUG: print(module, random_name, ' -> ', symbol)
            setattr(module, symbol, value)
            delattr(module, random_name)

    @contextmanager
    def randomized_filename(self, filename):
        '''Return a 'with' context to randomize a filename before using it. (yield version)'''
        import tempfile, os, os.path
        name, ext = filename.split('.')                                                                                             
        randomized = next(tempfile._get_candidate_names()) + '.' + ext                                                         
        if os.path.isfile(filename):
            if DEBUG: print(filename, ' -> ', randomized)
            os.rename(filename, randomized)
            try:
                yield
            finally:
                if DEBUG: print(self.filename, ' <- ', self.randomized)
                os.rename(self.randomized, self.filename)

    # FIXME: usare assertEqual che da un messaggio più leggibile
    # DEPRECATED
    def check(self, value, expected, params=None, explanation=''):
        # TODO: add deepcopy of value to avoid side effects
        msg = ''
        if params:
            msg += '\twhen input={} '.format(params)
        msg += '\n\t\t%r != %r' % (value, expected)
        if explanation:
            msg += "\t<- " + explanation
        self.assertEqual(value, expected, msg)

    def check_text_file(self,a,b):
        with open(a, encoding='utf8') as f: txt_a = f.read()
        with open(b, encoding='utf8') as f: txt_b = f.read()
        lines_a = [l.strip() for l in txt_a.splitlines()]
        lines_b = [l.strip() for l in txt_b.splitlines()]
        # TODO: usare una diff
        msg = 'The texts differ: ' + a + ' ' + b
        self.assertEqual(lines_a, lines_b, msg)

    def __image_load(self, filename):
        '''Load the PNG image from the PNG file under 'filename',
            convert it into tuple-matrix format and return it'''
        import png
        with open(filename,'rb') as f:
            # the file is read as a 256-colour RGB (without transparency)
            reader = png.Reader(file=f)
            w, h, png_img, _ = reader.asRGB8()
            # the list of lists is converted to tuples
            # the PNG colors are 3 consecutive values of the png_img array
            w *= 3
            return [ [ (line[i],line[i+1],line[i+2]) 
                       for i in range(0, w, 3) ]
                     for line in png_img ]

    def check_img_file(self, a, b):
        if not os.path.exists(a):
            self.assertEqual(0, 1, f"L' immagine di output non e' stata salvata in {a}\nThe output image was not saved in {a}")
        f = open(a, "rb")
        g = open(b, "rb")
        if sha1(f.read()).hexdigest() !=  sha1(g.read()).hexdigest():
            img_a = self.__image_load(a)
            img_b = self.__image_load(b)
            wa, ha = len(img_a[0]),len(img_a)
            wb, hb = len(img_b[0]),len(img_b)
            self.assertEqual(wa, wb, f"Images have different widths ({wa} != {wb})")
            self.assertEqual(ha, hb, f"Images have different heights ({ha} != {hb})")
            for y in range(ha):
                for x in range(wa):
                    ca, cb = img_a[y][x], img_b[y][x] 
                    msg = 'Images differ, starting at coordinates {},{} (colors: {} != {})'.format(x, y, ca, cb)
                    self.assertEqual(ca, cb, msg)
        f.close()
        g.close()

    def check_json_file(self, a, b, msg='The JSON files contain different structures'):
        import json
        with open(a,'r', encoding='utf8') as f1:
            A = json.load(f1)
        with open(b,'r', encoding='utf8') as f2:
            B = json.load(f2)
        self.assertEqual(A, B, msg)

    def check_json_file_to_list(self, jsonf, result, msg=(f'\n{"*"*100}\n README: The list of all generated images is ' 
                                                          f'NOT correct.\nthe FIRST set mentioned above is the EXPECTED; '
                                                          f'SECOND set is your RESULT\n'
                                                          f'> "Items in the first set but not the second"\n\tMEANS' 
                                                          f' you are MISSING some useful images\n'
                                                          f'> "Items in the second set but not the first"\n\tMEANS you are generating TOO '
                                                          f'many images with not useful properties\n{"*"*100}')                                
                                ):
        import json
        with open(jsonf, 'r', encoding='utf8') as fr:
            expected = json.load(fr)['expected']
        expected_s = tuple(tuple(tuple(c for c in row) for row in mat) for mat in expected)
        expected_s = set(expected_s)
        result_s = set(result)
        self.assertSetEqual(expected_s, result_s, msg)
  
    def should_skip(self, reason):
        'skip a test if main is called with skipSome=True'
        if self.__skipSome:
            self.skipTest(reason)

    def check_types_present(self,types):
        '''check that the functions/methods typer are the one passed as argument'''
        import program01
        for fname,t in types.items():
            f = getattr(program01, fname)
            self.assertEqual(f.__annotations__, t, 
                             f"le annotazioni di tipo di '{fname}' sono state modificate / the type annotations of '{fname}' have been changed")

    @staticmethod
    def isVar( X ):
        "riconosce le variabli (tutto tranne routine, classi, funzioni, moduli)"
        import inspect
        return (    not inspect.isroutine(X)
                and not inspect.isfunction(X)
                and not inspect.isclass(X)
                and not inspect.ismodule(X))

    def check_no_mutable_globals(self, module):
        '''check that the module does not contain global variables with mutable arguments'''
        import inspect
        ignore= [ '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__annotations__', '__warningregistry__',]
        errors = []
        VARS = inspect.getmembers(module, TestCase.isVar)
        VARS = list(filter(lambda x: x[0] not in ignore, VARS))
        for nv,v in VARS:
            if TestCase.isMutable(v):
                errors.append(f"GLOBAL VARIABLE DETECTED: {nv}={v}")
        if errors:
            raise ForbiddenError('Global variables with mutable values could introduce side-effects and are forbidden.\n\t'+'\n\t'.join(errors))

    @staticmethod
    def isMutable( X ):
        """All is mutable except for immutable base types and immutable containers with immutable contents"""
        from types import MappingProxyType
        immutable      = ( type(None), str, int, float, bool, bytes, bytearray, complex, memoryview )
        imm_containers = ( frozenset, tuple )
        imm_dicts      = ( MappingProxyType, )
        if isinstance(X, immutable):
            return False
        if isinstance(X, imm_containers):
            return any( TestCase.isMutable(Y) for Y in X )
        if isinstance(X, imm_dicts):
            return any( TestCase.isMutable(Y) for Y in X.values())
        return True

    def check_no_global_keyword(self, filename):
        import ast
        with open(filename, encoding='utf8') as F:
            code = F.read()
        T = ast.parse(code)
        errors = []
        for node in ast.walk(T):
            if isinstance(node, ast.Global):
                names = ", ".join(node.names)
                errors.append(f"DETECTED 'global {names}' in {filename} at line {node.lineno}")
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'globals':
                errors.append(f"DETECTED 'globals()' call in {filename} at line {node.lineno}")
            if isinstance(node, ast.Name) and node.id in ['__builtins__', '__builtin__']:
                errors.append(f"DETECTED '__builtins__' access in {filename} at line {node.lineno}")
            # FIXME: altro?
        if errors:
            raise ForbiddenError('Changing global variables is forbidden.\n\t'+'\n\t'.join(errors))

    def check_no_mutable_defaults(self, module):
        import inspect
        def get_defaults( ff ):
            signature = inspect.signature(ff)
            return {    k: v.default for k,v in signature.parameters.items() 
                                     if v.default is not inspect.Parameter.empty }
        errors = []
        FUNS = inspect.getmembers(module, inspect.isroutine)
        # TODO: retrieve also inner functions
        for nf,f in FUNS:
            for k,v in get_defaults(f).items():
                if TestCase.isMutable(v):
                    errors.append(f"DETECTED MUTABLE DEFAULT in {nf}: ({k}={v})")
        CLSS = inspect.getmembers(module, inspect.isclass)
        for nc,c in CLSS:
            METS = inspect.getmembers(c, inspect.isfunction)
            # TODO: retrieve also inner functions
            for nm, m in METS:
                for k,v in get_defaults(m).items():
                    if TestCase.isMutable(v):
                        errors.append(f"DETECTED MUTABLE DEFAULT in {nc}.{nm}: ({k}={v})")
        if errors:
            raise ForbiddenError('Mutable defaults could produce hard to find errors and are forbidden.\n\t'+'\n\t'.join(errors))

    def check_no_class_variables(self, module):
        import inspect
        cignore= [ '__hash__', '__weakref__', '__doc__', '__module__', '__dict__', '__args__', '__parameters__', '__annotations__',
                  '__cause__', '__context__', '__traceback__', '__suppress_context__' ]
        errors = []
        CLSS = inspect.getmembers(module, inspect.isclass)
        for nc,c in CLSS:
            VARS = inspect.getmembers(c, TestCase.isVar)
            VARS = list(filter(lambda x: x[0] not in cignore, VARS))
            for nv,v in VARS:
                errors.append(f"DETECTED CLASS VARIABLE {nc}.{nv}={v}")
        if errors:
            raise ForbiddenError('Class variables could be used for caching and are forbidden.\n\t'+'\n\t'.join(errors))

    @classmethod
    def main(cls,skipSome=False):
        cls.__skipSome = skipSome             # pass True to skip some test while timing
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
        result = runner.run(suite)
        failed = len(result.failures)
        passed = result.testsRun-failed
        print("{} test passed, {} tests failed".format(passed, failed))  

