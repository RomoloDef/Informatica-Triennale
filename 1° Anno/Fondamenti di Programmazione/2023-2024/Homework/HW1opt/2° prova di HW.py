
"""
Created on Sat Oct 21 11:49:14 2023

@author: romolodeffereria
"""


''' 
Abbiamo una stringa int_seq contenente una sequenza di interi non-negativi
    separati da virgole ed un intero positivo subtotal.

Progettare una funzione ex1(int_seq, subtotal) che
    riceve come argomenti la stringa int_seq e l'intero subtotal e
    restituisce il numero di sottostringhe di int_seq
    la somma dei cui valori è subtotal.

Ad esempio, per int_seq='3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2' e subtotal=9,
    la funzione deve restituire 7.

Infatti:
'3,0,4,0,3,1,0,1,0,1,0,0,5,0,4,2'
 _'0,4,0,3,1,0,1,0'_____________
 _'0,4,0,3,1,0,1'_______________
 ___'4,0,3,1,0,1,0'_____________
____'4,0,3,1,0,1'_______________
____________________'0,0,5,0,4'_
______________________'0,5,0,4'_
 _______________________'5,0,4'_

NOTA: è VIETATO usare/importare ogni altra libreria a parte quelle già presenti

NOTA: il timeout previsto per questo esercizio è di 1 secondo per ciascun test (sulla VM)

ATTENZIONE: quando caricate il file assicuratevi che sia nella codifica UTF8
    (ad esempio editatelo dentro Spyder)
'''

def ex1(int_seq, subtotal):
 #trasformo la lista, in una lista di numeri interi e tramite la funzione replace tolgo la virgola dalla lista
 int_seq = list(map(int, int_seq.replace(",", " ")))
 #la variabile somma_C serve per contare le somme all'interno della lista
 somma_C = [0]
 #la variabile contatore invece serve per contare il numero di sottostringhe
 contatore = 0
 for numero in int_seq:
    somma_C.append(somma_C[-1]+ numero)
    # j>i
    for i in range(len(somma_C)):
            for j in range(i+1, len(somma_C)):
                if subtotal == somma_C[j]-somma_C[i]:
                    #se questa condizione è vera allora il numero di sottostringhe da contare incrementa sempre di uno
                    contatore = contatore + 1
                    
                    return contatore


if __name__ == '__main__':
    import testlib
    import random
    from ddt import file_data, ddt, data, unpack

    import program01 as program

    @ddt
    class Test(testlib.TestCase):

        def do_test(self, test_int_seq, test_subtotal, expected):
            """Test implementation
            - test_int_seq: input string
            - test_subtotal: input number
            - expected: expected output
            TIMEOUT: 1 second for each test
            """
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.timeout(1), \
                    self.timer(1):
                result = program.ex1(test_int_seq, test_subtotal)
            self.assertEqual(type(result), int,
                             ('The output type should be: int\n'
                              '[Il tipo di dato in output deve essere: int]'))
            self.assertEqual(result, expected,
                             ('The return value is incorrect\n'
                              '[Il valore di ritorno è errato]'))
            return 1

        @file_data("test_01.json")
        def test_1_S1(self, test_int_seq, test_subtotal, expected):
            return self.do_test(test_int_seq, test_subtotal, expected)

        def test_many_zeros_1000(self):
            """Test with a string having 1000 0’s and
            250,000 sequences such that
            the sum of their values is equal to 2
            [Test con una stringa avente 1000 zeri e
             250.000 sequenze tali che
             la somma dei loro valori sia uguale a 2]"""
            test_seq_len  = 1000
            half          = test_seq_len // 2
            zeros         = ['0'] * (half-1)
            test_int_seq  = ",".join(zeros + ['1']*2 + zeros)
            test_subtotal = 2
            expected      = half ** 2
            return self.do_test(test_int_seq, test_subtotal, expected)

        def test_many_1s(self):
            """Test with a string having 20,000 1’s and
            19,001 sequences such that
            the sum of their values is equal to 1000
            [Test con una stringa avente 20,000 valori uguali a 1 e
             19.001 sequenze tali che
             la somma dei loro valori sia uguale a 1000]"""
            test_seq_len  = 20000
            test_int_seq  = ",".join(['1'] * test_seq_len)
            test_subtotal = 1000
            expected      = test_seq_len - test_subtotal + 1
            return self.do_test(test_int_seq, test_subtotal, expected)

        def test_many_internal_zeros(self):
            """Test with a string having 1,000 0’s and
            1 sequence such that
            the sum of its values is equal to 2
            [Test con una stringa avente 1000 zeri ed
             1 sequenza tale che
             la somma dei suoi valori sia uguale a 2]"""
            test_seq_len  = 1000
            zeros         = ['0'] * test_seq_len
            test_int_seq  = ",".join(['1'] + zeros + ['1'])
            test_subtotal = 2
            expected      = 1
            return self.do_test(test_int_seq, test_subtotal, expected)
        
    if __name__ == '__main__':
        Test.main()

import time, sys
import stopit
import unittest, unittest.mock

class ForbiddenError(Exception):
    pass

class TimeoutError(Exception):
    pass

class Timer:
    def __init__(self, timeout):
        self.timeout = timeout

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        wallclock_time = round(time.time() - self.start, 3)
        if wallclock_time > self.timeout:
            raise TimeoutError(f'Timeout! ({wallclock_time} > {self.timeout})')


class TestCase(unittest.TestCase):
    __orig_import = __builtins__['__import__']
    __orig_open   = __builtins__['open']

    def _raise_forbidden(self, forbidden):
        # Lamdable method that throws an exception
        raise ForbiddenError(f"The usage of the '{forbidden}' function/method is forbidden!")

    def forbidden_function(self, target='os.walk'):
        # Return a 'with' context to forbid using a target function: by default 'os.walk'
        return unittest.mock.patch(target, new=lambda *x, **k: self._raise_forbidden( target ))

    def check_imports(self, allowed=[], forbidden=[]):
        # Return a 'with' context to forbid imports not listed in 'allowed' or listed in 'forbidden'
        def _check_import(*args, **kargs):
            name = args[0]
            if name in forbidden or (not forbidden and name not in allowed):
                print(f"Importing {name} ({kargs}) (not allowed)")
                raise ForbiddenError(f"The import of '{name}' is forbidden")
            else:
                # print(f"Importing {name} ({kargs}) (allowed)")
                return self.__orig_import(*args, **kargs)
        return unittest.mock.patch('builtins.__import__', new=_check_import)

    def check_open(self, allowed_filenames_modes=None):
        if not allowed_filenames_modes:
            allowed_filenames_modes = {}
        def _check_open(*args, **kargs):
            if len(args) > 1:
                mode = args[1]
            else:
                mode = kargs.get('mode', 'r')
            filename = args[0]
            # print(f"checking {filename} ({args}, {kargs}) against {allowed_filenames_modes}")
            if filename not in allowed_filenames_modes:
                print(f"Opening file '{filename}' is not allowed!")
                raise ForbiddenError(f"It's forbidden to open file '{filename}'")
            if mode not in allowed_filenames_modes[filename]:
                print(f"Opening file '{filename}' with mode '{mode}' is not allowed!")
                raise ForbiddenError(f"Opening file '{filename}' with mode='{mode}' is forbidden!")
            # print(f"Opening file {filename} with mode {mode} (allowed)")
            return self.__orig_open(*args, **kargs)
        return unittest.mock.patch('builtins.open', new=_check_open)

    def ignored_function(self, target='builtins.print'):
        # Return a 'with' context that ignores a target function: by default 'builtins.print'
        return unittest.mock.patch(target, new=lambda *x, **k: None)

    def timer(self, sec):
        '''Return a context in which the execution time is measured and, if necessary, a time-out exception is thrown.
        This way, the timeout is detected even if the timeout signal is captured.'''
        return Timer(sec)

    def timeout(self, sec):
        '''Return a 'with' context to stop the code when the timeout expires.'''
        return stopit.ThreadingTimeout(sec, swallow_exc=False)
        #return stopit.SignalTimeout(sec, swallow_exc=False)

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

    def check_img_file(self, a,b):
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

    def check_json_file(self, a, b, msg='The JSON files contain different structures'):
        import json
        with open(a,'r', encoding='utf8') as f1:
            A = json.load(f1)
        with open(b,'r', encoding='utf8') as f2:
            B = json.load(f2)
        self.assertEqual(A, B, msg)

    @classmethod
    def main(cls):
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(cls))
        runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=2)
        result = runner.run(suite)
        failed = len(result.failures)
        passed = result.testsRun-failed
        print("{} test passed, {} tests failed".format(passed, failed))  


# Inserisci qui i tuoi test personali
    pass

