import testlib
from ddt import ddt, data, unpack, file_data

# change this variable to True to disable timeout and enable print
DEBUG = False
#DEBUG = True

WARP = 1     # speed warp for student's PC
#WARP= 2     # uncomment for the Virtual Machine
TIMEOUT = 0.5 * WARP # VM warp factor


@ddt
class Test(testlib.TestCase):
    def do_test(self, bases, expected):
        """Test implementation
        - bases:		list of bases (integers > 1)
        - expected:		expected result
        TIMEOUT: 1 seconds for each test
        """
        if DEBUG:
                import program01 as program
                result = program.find_doubles(bases)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io', 'typing']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.find_doubles(bases)
        self.assertSetEqual(result, set(expected), 
                            (f"The set of result numbers is different"
                             "than the set of expected ones\n",
                             f"L'insieme dei numeri tornati nel risultato"
                             "non corrisponde all'insieme dei valori"
                             "attesi"))
        return 1

    def test_intricacy(self):
        self.check_max_ciclomatic_complexity()

    def test_zz_top_types(self):
        self.should_skip('skipped during timing')
        from typeguard import install_import_hook
        try:
            import sys
            del sys.modules['program01']
        except:pass
        with install_import_hook('program01'):
            import program01
            self.test_00_decode_example()

    def test_00_decode_example(self):
        import program01 as program
        bases = [2, 3, 4]
        digits = [1, 1, 2]
        expected = 36
        result = program.decode_digits(digits, bases)
        self.assertEqual(result, expected)

    @data (
        # bases                           digits          expected
        ([3, 4],                         [2, 2],          10),
        ([2, 5, 10],                     [1, 4, 9],       921),
        ([2, 5, 10],                     [1, 2, 1],       111),
        ([2, 5, 10],                     [0, 0, 9],       900),
        ([9, 9, 9],                      [0, 0, 0],       0),
        ([9, 8, 9, 8],                   [8, 7, 8, 7],    4296),
        ([2, 2, 2, 2, 2],                [1, 1, 1, 1, 1],    31),
        ([6, 6, 6, 6, 6],                [3, 0, 1, 2, 5], 6951),
    )
    @unpack
    def test_01_decode_digits(self, bases, digits, expected):
        import program01 as program
        result = program.decode_digits(digits, bases)
        self.assertEqual(result, expected)

    # Per vedere i casi di tesi della funzione generate_digits
    # aprire il file generate_digits.json come un file di testo
    # ---------------------------------------------------------
    # To see the test case for the function generate_digits
    # please open the file generate_digits.json as a txt file
    @file_data("generate_digits.json")
    def test_02_generate_digits(self, base, comb):
        import program01 as program
        generated = program.generate_digits(base)
        self.assertSetEqual(set(tuple(L) for L in generated),
                            set(tuple(L) for L in comb))


    @data(
        ([2, 5], []),
        ([4, 3, 2], [3, 4, 5, 6, 7, 8, 9, 10]),
        ([2, 2], []),
        ([2, 5, 10], []),
        ([8, 4, 2], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
        ([5, 4, 3], [4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 30]),
        ([5, 4, 3, 2], [4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 38]),
        ([3, 2, 3, 3, 7], [2, 4867, 12034, 9606, 14471, 2439, 11, 4876, 12043, 9615, 14480, 2448, 20, 12052, 9624, 2457, 29, 12061, 9633, 2466, 7205, 38, 12070, 9642, 2475, 7214, 47, 12079, 9651, 7223, 56, 9660, 7232, 65, 2430, 4804, 9669, 14408, 7241, 74, 4813, 9678, 14417, 7250, 4822, 14426, 7259, 4831, 14435, 2403, 7268, 12007, 4840, 14444, 2412, 7277, 12016, 4849, 14453, 2421, 12025, 4858, 14462]),
        ([50, 15], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244]),
    )
    @unpack
    def test_03_find_doubles(self, bases, expected):
        import program01 as program
        doubles = program.find_doubles(bases)
        #print(doubles)
        self.assertSetEqual(doubles, set(expected))

    ######################### SECRET TESTS START HERE! #########################
        
if __name__ == '__main__':
    Test.main()

