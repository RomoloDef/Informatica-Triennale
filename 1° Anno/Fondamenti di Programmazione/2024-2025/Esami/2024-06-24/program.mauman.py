#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER

To pass the exam you must:
    - solve at least 3 exercises of type func AND;
    - solve at least 1 exercise of type ex (recursive problem) AND;
    - obtain a score greater than or equal to 18

The final grade is the sum of the scores of the solved problems.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

name = "Maurizio"
surname = "Mancini"
student_id = "12345678"


# %% ----------------------------------- FUNC1 ------------------------- #
'''func1: 2 points
Define the function func1(L) that takes as input a list of lists of characters.
The function returns the list of characters that do not repeat inside each
of the inner lists.
For example, given the list L = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
the function returns the list ['a', 'b', 'c', 'c']
as 'a' does not repeats in the list ['e', 'a', 'e']
'b' and 'c' do not repeat in the list ['b', 'c']
and 'c' does not repeat in the list ['c', 'd', 'd'].
'''
def func1(L):
    result = []
    for inner in L:
        for i, c in enumerate(inner):
            if c not in inner[:i] + inner[i + 1:]:
                result.append(c)
    return result

# L = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
# print(func1(L))
# L = [['a', 'b', 'b', 'b', 'a'], ['z', 'y', 'x', 'w', 'v'], ['a']]
# print(func1(L))
# L = [['a', 'a', 'b', 'b', 'c', 'a', 'b', 'c', 'd']]
# print(func1(L))
# L = [['a', 'b', 'c', 'a', 'b', 'c'], ['z', 'y', 'x', 'x', 'z', 'y'], ['a', 'b', 'a', 'b'], ['z', 'z']]
# print(func1(L))

# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 2 points
Define a function func2(L0, L1) that receives 2 lists L0 and L1.
The first list L0 contains strings S0, S1, ... Sn-1,
the second list L1 contains positive integers I0, I1, ... In-1.
The function returns a string obtaining by concatenating each string
Sj repeated Ij times.
For example, if L0 = ['ab', 'o o'] and L1 = [2, 3] the function returns:
'ababo oo oo o'.
'''
def func2(L0, L1):
    result = ""
    for pair in list(zip(L0, L1)):
        result += pair[0] * pair[1]
    return result

# L0 = ['ab', 'o o']
# L1 = [2, 3]
# print(func2(L0, L1))
# L0 = ['quick', 'brow', 'fox']
# L1 = [2, 0, 2]
# print(func2(L0, L1))
# L0 = ['h', 'e', 'l', 'o']
# L1 = [1, 1, 2, 1]
# print(func2(L0, L1))
# L0 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# print(func2(L0, L1))

# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 points
Define a function func3(file_in) that reads a text file.
The file contains integer numbers separated by (multiple) spaces and on different lines.
The function returns the sum of the numbers on even lines minus the sum
of the numbers on odd lines. The first line in the file is line 0, so it
is an even line; the second line is line 1, so it is odd; and so on.
For example, if the file contains:
   4        1 2     -3
0   1        -2         
       10
 -5          6

the function returns 14, as 14=(4+1+2-3+10)-(0+1-2-5+6)
'''

def func3(file_in):
    F = open(file_in, "r", encoding="utf-8")
    counter = 0
    sum_even = 0
    sum_odd = 0
    for line in F:
        nums = line.strip().split(" ")
        N = []
        for n in nums:
            if n != "":
                N.append(int(n))
        if counter % 2 == 0:
            sum_even += sum(N)
        else:
            sum_odd += sum(N)
        counter += 1
    F.close()
    return sum_even - sum_odd

# print(func3("func3/in1.txt"))
# print(func3("func3/in2.txt"))
# print(func3("func3/in3.txt"))
# print(func3("func3/in4.txt"))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2 points
Define a function func4(D) that receives as input a dictionary, in which
each key is a string and the corrisponding value is a collection
(a set, a dictionary, a list, ...).
The function returns a list of lists, in which each sublist S corresponds
to an item of the input dictionary and contains the following:
- as first item I0, the key of the corresponding dictionary item
- as second item I1, the value of the corresponding dictionary item
The sublists are sorted by the length of the second item I1 in each sublists,
in reversed order (from the longest to the shortest).
If the two sublists have a second item with the same length, they are sorted
based on the value of the first item I0 (alphabetically, or numerically).
For example, if D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
the function returns: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
"""

def func4(D):
    result = []
    for k in D:
        result.append([k, D[k]])
    result.sort(key=lambda x:(-len(x[1]), x[0]))
    return result

# D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
# print(func4(D))
# D = {3: {'name': 'Steve', 'age': 25, 'marks': 60}, 2: {'name': 'Anil', 'age': 23, 'marks': 75}, 1: {'name': 'Asha', 'age': 20, 'marks': 70}}
# print(func4(D))
# D = {'hp': {'name': ' Folio Elitebook 9470M', 'brand': 'HewlettPackard Laptop', 'price':30000},
#             'lenovo': {'name': 'Camera 8989', 'brand': 'Lenovo Laptop', 'price':40000},
#             'dell': {'name': 'Dell Inspiron', 'brand': 'Dell Laptop', 'price':200}}
# print(func4(D))
# cities = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch", "Apple Valley", "Appleton", "Arlington", "Arvada", "Asheville", "Athens", "Atlanta", "Atlantic City", "Augusta", "Aurora", "Austin", "Bakersfield", "Baltimore", "Barnstable", "Baton Rouge", "Beaumont", "Bel Air", "Bellevue", "Berkeley", "Bethlehem", "Billings", "Birmingham", "Bloomington", "Boise", "Boise City", "Bonita Springs", "Boston", "Boulder", "Bradenton", "Bremerton", "Bridgeport", "Brighton", "Brownsville", "Bryan", "Buffalo", "Burbank", "Burlington", "Cambridge", "Canton", "Cape Coral", "Carrollton", "Cary", "Cathedral City", "Cedar Rapids", "Champaign", "Chandler", "Charleston", "Charlotte", "Chattanooga", "Chesapeake", "Chicago", "Chula Vista", "Cincinnati", "Clarke County", "Clarksville", "Clearwater", "Cleveland", "College Station", "Colorado Springs", "Columbia", "Columbus", "Concord", "Coral Springs", "Corona", "Corpus Christi", "Costa Mesa", "Dallas", "Daly City", "Danbury", "Davenport", "Davidson County", "Dayton", "Daytona Beach", "Deltona", "Denton", "Denver", "Des Moines", "Detroit", "Downey", "Duluth", "Durham", "El Monte", "El Paso", "Elizabeth", "Elk Grove", "Elkhart", "Erie", "Escondido", "Eugene", "Evansville", "Fairfield", "Fargo", "Fayetteville", "Fitchburg", "Flint", "Fontana", "Fort Collins", "Fort Lauderdale", "Fort Smith", "Fort Walton Beach", "Fort Wayne", "Fort Worth", "Frederick", "Fremont", "Fresno", "Fullerton", "Gainesville", "Garden Grove", "Garland", "Gastonia", "Gilbert", "Glendale", "Grand Prairie", "Grand Rapids", "Grayslake", "Green Bay", "GreenBay", "Greensboro", "Greenville", "Gulfport-Biloxi", "Hagerstown", "Hampton", "Harlingen", "Harrisburg", "Hartford", "Havre de Grace", "Hayward", "Hemet", "Henderson", "Hesperia", "Hialeah", "Hickory", "High Point", "Hollywood", "Honolulu", "Houma", "Houston", "Howell", "Huntington", "Huntington Beach", "Huntsville", "Independence", "Indianapolis", "Inglewood", "Irvine", "Irving", "Jackson", "Jacksonville", "Jefferson", "Jersey City", "Johnson City", "Joliet", "Kailua", "Kalamazoo", "Kaneohe", "Kansas City", "Kennewick", "Kenosha", "Killeen", "Kissimmee", "Knoxville", "Lacey", "Lafayette", "Lake Charles", "Lakeland", "Lakewood", "Lancaster", "Lansing", "Laredo", "Las Cruces", "Las Vegas", "Layton", "Leominster", "Lewisville", "Lexington", "Lincoln", "Little Rock", "Long Beach", "Lorain", "Los Angeles", "Louisville", "Lowell", "Lubbock", "Macon", "Madison", "Manchester", "Marina", "Marysville", "McAllen", "McHenry", "Medford", "Melbourne", "Memphis", "Merced", "Mesa", "Mesquite", "Miami", "Milwaukee", "Minneapolis", "Miramar", "Mission Viejo", "Mobile", "Modesto", "Monroe", "Monterey", "Montgomery", "Moreno Valley", "Murfreesboro", "Murrieta", "Muskegon", "Myrtle Beach", "Naperville", "Naples", "Nashua", "Nashville", "New Bedford", "New Haven", "New London", "New Orleans", "New York", "New York City", "Newark", "Newburgh", "Newport News", "Norfolk", "Normal", "Norman", "North Charleston", "North Las Vegas", "North Port", "Norwalk", "Norwich", "Oakland", "Ocala", "Oceanside", "Odessa", "Ogden", "Oklahoma City", "Olathe", "Olympia", "Omaha", "Ontario", "Orange", "Orem", "Orlando", "Overland Park", "Oxnard", "Palm Bay", "Palm Springs", "Palmdale", "Panama City", "Pasadena", "Paterson", "Pembroke Pines", "Pensacola", "Peoria", "Philadelphia", "Phoenix", "Pittsburgh", "Plano", "Pomona", "Pompano Beach", "Port Arthur", "Port Orange", "Port Saint Lucie", "Port St. Lucie", "Portland", "Portsmouth", "Poughkeepsie", "Providence", "Provo", "Pueblo", "Punta Gorda", "Racine", "Raleigh", "Rancho Cucamonga", "Reading", "Redding", "Reno", "Richland", "Richmond", "Richmond County", "Riverside", "Roanoke", "Rochester", "Rockford", "Roseville", "Round Lake Beach", "Sacramento", "Saginaw", "Saint Louis", "Saint Paul", "Saint Petersburg", "Salem", "Salinas", "Salt Lake City", "San Antonio", "San Bernardino", "San Buenaventura", "San Diego", "San Francisco", "San Jose", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Maria", "Santa Rosa", "Sarasota", "Savannah", "Scottsdale", "Scranton", "Seaside", "Seattle", "Sebastian", "Shreveport", "Simi Valley", "Sioux City", "Sioux Falls", "South Bend", "South Lyon", "Spartanburg", "Spokane", "Springdale", "Springfield", "St. Louis", "St. Paul", "St. Petersburg", "Stamford", "Sterling Heights", "Stockton", "Sunnyvale", "Syracuse", "Tacoma", "Tallahassee", "Tampa", "Temecula", "Tempe", "Thornton", "Thousand Oaks", "Toledo", "Topeka", "Torrance", "Trenton", "Tucson", "Tulsa", "Tuscaloosa", "Tyler", "Utica", "Vallejo", "Vancouver", "Vero Beach", "Victorville", "Virginia Beach", "Visalia", "Waco", "Warren", "Washington", "Waterbury", "Waterloo", "West Covina", "West Valley City", "Westminster", "Wichita", "Wilmington", "Winston", "Winter Haven", "Worcester", "Yakima", "Yonkers", "York", "Youngstown"]
# D = {char: {city for city in cities if city.startswith(char)} for char in 'ABCDEFGHIJKLMNOPRSTUVWY'}
# print(func4(D))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Define a function func5(file_in, file_out) that reads the file_in file
containing an image, using the load function in the images package.
The image is represented as a list of lists of pixels, each pixel is
a tuple (r, g, b), and the inner lists represent the rows of the image.
The image has a black background and some non-black diamonds and Xs
drawn on it, such as (if a dot represents a black pixel and a star
represents a non-black pixel):

            .*.
diamond =   *.*
            .*.


X =         *.*
            .*.
            *.*

Each diamond or X is such that the 3x3 area occupied by its pixels
is spaced by 1 pixel in every direction, respect to each of the other
diamonds and Xs in the image.
After reading the image, the function transforms all the diamonds into
Xs and vice-versa, without modifying their color (all the pixels in a diamond or X
have the same color).
Finally, the function saves the resulting image into the file_out file
using the save function in the images package and returns a tuple
(a, b), where a is the number diamonds and b is the number of Xs in the
input image.
"""
import images

def func5(file_in, file_out):
    black = (0, 0, 0)
    img = images.load(file_in)
    width = len(img[0])
    height = len(img)
    img_res = [[black for j in range(width)] for i in range(height)]
    count_d = 0
    count_x = 0
    for i in range(height):
        for j in range(width):
            if img[i][j] != black:
                if j < width - 2 and img[i][j + 2] != black:
                    # it's a X
                    count_x += 1
                    img_res[i][j + 1] = img[i][j]
                    img_res[i + 1][j] = img[i][j]
                    img_res[i + 1][j + 2] = img[i][j]
                    img_res[i + 2][j + 1] = img[i][j]
                    img[i][j] = black
                    img[i][j + 2] = black
                    img[i + 1][j + 1] = black
                    img[i + 2][j] = black
                    img[i + 2][j + 2] = black
                else:
                    count_d += 1
                    # it's a diamond
                    img_res[i][j - 1] = img[i][j]
                    img_res[i][j + 1] = img[i][j]
                    img_res[i + 1][j] = img[i][j]
                    img_res[i + 2][j - 1] = img[i][j]
                    img_res[i + 2][j + 1] = img[i][j]
                    img[i][j] = black
                    img[i + 1][j - 1] = black
                    img[i + 1][j + 1] = black
                    img[i + 2][j] = black
    images.save(img_res, file_out)
    return (count_d, count_x)
                    
    

# print(func5("func5/img0_in.png", "func5/img0_out.png"))
# print(func5("func5/img1_in.png", "func5/img1_out.png"))
# print(func5("func5/img2_in.png", "func5/img2_out.png"))
# print(func5("func5/img3_in.png", "func5/img3_out.png"))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(), recursive or using recursive functions
or methods, that, given a list of N lists of M characters each, builds and returns
the list of all the possible strings of N characters obtained by concatenating
a character from the first list, another one from the second, the third, and so on.
For example, if the input list is: [['c', 'q', 'a'], ['w', 'e', 'y']],
the function returns: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy']
The returned list must be sorted in alphabetical order.
"""

def rec_build(l0, l1):
    if l1 == []:
        return l0
    res = []
    for i0 in l0:
        for i1 in l1[0]:
            res.append(i0 + i1)
    return rec_build(res, l1[1:])
        

def ex1(L):
    return sorted(rec_build([''], L))

# L = [['c', 'q', 'a'], ['w', 'e', 'y']]
# print(ex1(L))
# L = [['0', '1'], ['0', '1'], ['0', '1'], ['0', '1']]
# print(ex1(L))
# L = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
# print(ex1(L))
# L = [['0', '1', '2'], ['a', 'b', 'c'], ['0', '1', '2'], ['x', 'y', 'z']]
# print(ex1(L))


# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 8 points

Define a function ex2(root), recursive or using recursive functions
or methods, that takes a binary tree as input and modifies it (in-place) by
recursively adding to each node the values of its child nodes (if any).
The sum must be done bottom-up, that is, leaves will be added to
their parent nodes, and so on, until the root is reached.
The function returns the number of odd and even values in the original
tree.
If the input tree is:

               1
              / \
             2   3
            /   / \
           4   5   6
              /
             7
The modified tree will be:
               28
              /  \
             6    21
            /    / \
           4    12  6
               /
              7
and the function will return (4, 3).
"""

import tree

def rec_add(root, odd, even):
    if root.left is None and root.right is None:
        if root.value % 2 == 0:
            return (root.value, odd, even + 1)
        else:
            return (root.value, odd + 1, even)
    if root.value % 2 == 0:
        even += 1
    else:
        odd += 1
    if root.left is not None:
        childresult = rec_add(root.left, odd, even)
        root.value += childresult[0]
        odd = childresult[1]
        even = childresult[2]
    if root.right is not None:
        childresult = rec_add(root.right, odd, even)
        root.value += childresult[0]
        odd = childresult[1]
        even = childresult[2]
    return (root.value, odd, even)

def ex2(root):
    result = rec_add(root, 0, 0)
    return (result[1], result[2])

# T = tree.BinaryTree.fromList([1, [2, [4, None, None], None], [3, [5, [7, None, None], None], [6, None, None]]])
# print(ex2(T))
T = tree.BinaryTree.randomTree(15)
print(T.toList())
print(ex2(T))
# print(T)


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)