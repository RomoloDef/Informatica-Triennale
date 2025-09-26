import testlib, json
from ddt import ddt, data

# change this variable to True to disable timeout and enable print
DEBUG = True
DEBUG = False

@ddt
class Test(testlib.TestCase):

    def do_test(self, jsonfile):
        with open(jsonfile) as json_file:
            data = json.load(json_file)
        encrypted_text  = data['encrypted_text']
        pharaohs_cypher = data['pharaohs_cypher']
        expected        = set(data['expected'])            # convert list read from json to set
        time            = data['time']

        # timeout = 3 times my implementation on my laptop, with a minimum of 1 second
        TIMEOUT = max(3*time,1)  # *2           # VM warp factor
        if DEBUG:
            import program01 as program
            result = program.pharaohs_revenge(encrypted_text, pharaohs_cypher)
        else:
            with self.assertIsRecursive('program01') as program:
                   program.pharaohs_revenge(encrypted_text, pharaohs_cypher)
                   del program
            with   self.ignored_function('builtins.print'), \
                   self.ignored_function('pprint.pprint'), \
                   self.forbidden_function('builtins.input'), \
                   self.forbidden_function('builtins.eval'), \
                   self.check_imports(allowed=['program01', '_io','typing', 'tree','encodings.utf_8']), \
                   self.timeout(TIMEOUT), \
                   self.timer(TIMEOUT):
                import program01 as program
                result = program.pharaohs_revenge(encrypted_text, pharaohs_cypher)
        self.assertSetEqual(result, expected,
                         f"\n{'*'*10} [ENG] The output result {result} is not the expected {expected} {'*'*10}\n"
                         f"{'*'*10} [ITA] Il risultato {result} non è quello atteso {expected} {'*'*10}")

    def test_intricacy(self):
        self.check_max_ciclomatic_complexity()

    def test_untampered_types(self):
        tipi = { 'pharaohs_revenge': {
                        'encrypted_text'  : str,
                        'pharaohs_cypher' : dict[str,str],
                        'return'          : set[str]}
              }
        self.check_types_present(tipi)

    def test_example(self):
        jsonfile = 'tests/normal/example.json'
        self.do_test(jsonfile)

    def test_multichar(self):
        jsonfile = 'tests/normal/multichar.json'
        self.do_test(jsonfile)

    @data('1_3', '1_4', '1_5', '1_6', '1_7', '1_8', '2_3', '2_4', '2_5', '3_4', '4_3', 
          '2_4_new', '1_6_new', '3_4_new', '3_3_new' )
    def test_normal(self, test_id):
        jsonfile = f'tests/normal/test__{test_id}.json'
        self.do_test(jsonfile)

    ######################### SECRET TESTS START HERE! #########################

if __name__ == '__main__':
    Test.main()


