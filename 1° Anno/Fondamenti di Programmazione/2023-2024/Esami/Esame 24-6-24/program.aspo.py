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

name = "Aspo"
surname = "Aspo"
student_id = "Aspo"


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
    return [c for l in L for c in l if l.count(c) == 1]
    

L = [['e', 'a', 'e'], ['b', 'c'], ['c', 'd', 'd']]
print(func1(L))

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
    return ''.join([s*r for s, r in zip(L0, L1)])


L0 = ['ab', 'o o']
L1 = [2, 3]
print(func2(L0, L1))

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
    with open(file_in) as f:
        lines = f.readlines()
    return sum(sum(map(int, l.split())) for l in lines[0::2]) -\
        sum(sum(map(int, l.split())) for l in lines[1::2])

print(func3("func3/in1.txt"))

#%% ----------------------------------- FUNC4 ------------------------- #
""" func4: 2 points
Define a function func4(D) that receives as input a dictionary, in which
each key is a string.
The function returns a list of lists, in which each sublist corresponds
to an item in the dictionary, the first item of the list is the key and
the second item of the list is the corresponding value.
The list is sorted by the length of the second item of the sublists,
in reversed order (from the longest to the shortest).
If the second items of two or more sublists have the same length, they
are sorted by the first items (alphabetically).
For example, if D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
the function returns: [["f", (1, 2, 3)], ["a", ["h", "w"]], ["c", {"f":3, "g":[1,2]}]]
"""

def func4(D):
    return sorted(map(list, D.items()), key=lambda x: (-len(x[1]), x[0]))

D = {"f":(1, 2, 3), "a":["h", "w"], "c":{"f":3, "g":[1,2]}}
print(func4(D))

# %% ----------------------------------- FUNC5 ------------------------- #
""" func5: 8 points
Define a function func5(file_in, file_out) that reads the file_in file
containing an image, using the load function in the images package.
The image is represented as a list of lists of pixels, each pixel is
a tuple (r, g, b), and the inner lists represent the rows of the image.
The image has a black background and some non-black diamonds and Xs
drawn on it, such as (if a dot represents a black pixel and a star
represents a non-black pixel):

            -*-
diamond =   *-*
            -*-


X =         *-*
            -*-
            *-*

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
black = (0,0,0)

def x_to_diamond(im, i, j):
    color = im[i][j]
    im[i][j:j+3] = [black, color, black]
    im[i+1][j:j+3] = [color, black, color]
    im[i+2][j:j+3] = [black, color, black]

def diamond_to_x(im, i, j):
    color = im[i][j]
    im[i][j-1:j+2] = [color, black, color]
    im[i+1][j-1:j+2] = [black, color, black]
    im[i+2][j-1:j+2] = [color, black, color]

def func5(file_in, file_out):
    im = images.load(file_in)
    diamonds, xs = 0, 0
    modified = set()
    for i, row in enumerate(im):
        for j, pix in enumerate(row):
            if pix != black and (i,j) not in modified:
                # print (i, j, pix)
                if (j+2 < len(row) and im[i][j+2] !=black):
                    x_to_diamond(im, i, j)
                    xs += 1
                    # print("adding", {(x,y) for x in range(i, i+3) for y in range(j,j+3)})
                    modified.update({(x,y) for x in range(i, i+3) for y in range(j,j+3)})
                else:
                    diamond_to_x(im, i, j)
                    diamonds += 1
                    # print("adding", {(x,y) for x in range(i, i+3) for y in range(j-1,j+2)})
                    modified.update({(x,y) for x in range(i, i+3) for y in range(j-1,j+2)})
                # print(modified)
    images.save(im, file_out)
    return diamonds, xs
    
                    
    

print(func5("func5/img0_in.png", "func5/img0_out.png"))

# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 points

Define the function ex1(), recursive or using recursive functions
or methods, that, given a list of N lists of M characters each, builds and returns
the list of all the possible strings of N characters obtained by concatenating
a character from the first list, another one from the second, then thirs, and so on.
For example, if the input list is: [['c', 'q', 'a'], ['w', 'e', 'y']],
the function returns: ['ae', 'aw', 'ay', 'ce', 'cw', 'cy', 'qe', 'qw', 'qy']
The returned list must be sorted in alphabetical order.
"""

def _ex1(L):
    if len(L) == 1:
        return L[0]
    strings = []
    for c in L[0]:
        partial = ex1(L[1:])
        for p in partial:
            strings.append(c+p)
    return strings
            
def ex1(L):
    return sorted(_ex1(L))


L = [['c', 'q', 'a'], ['w', 'e', 'y'], ['w','v']]
print(ex1(L))
# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 points

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
def ex2(root):
    if root == None:
        return 0,0
    tot = root.value % 2, 1-root.value % 2
    if root.left:
        x, y = ex2(root.left)
        root.value += root.left.value
        tot = tot[0] +x, tot[1]+y
    if root.right:
        x, y = ex2(root.right)
        root.value += root.right.value
        tot = tot[0] +x, tot[1]+y
    return tot
        


T = tree.BinaryTree.fromList([1, [2, [4, None, None], None], [3, [5, [7, None, None], None], [6, None, None]]])
print(ex2(T))
print(T)


###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)