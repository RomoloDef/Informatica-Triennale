#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''It is a quiet December evening, and while it's pouring rain outside
you get a call from your friend Bart, who is not very computer
savvy. After calming him down, he tells you that he went to his PC to
look for the perfect gift, surfing on exotic and alternative
e-commerce sites, doing searches on disparate sites using an automatic
translator. He tells you he ended up on a site with the .atp domain,
thinking it had something to do with tennis, his great passion. After
following a couple of products on the strange site, he noticed that
his browser was responding more slowly and the mouse pointer was
starting to flicker. After a few seconds, a warning message appeared
informing him that he had been infected with the latest generation of
ransomware, which targets sensitive files. Panicked, he remembered
your venture with the Tarahumara sheet music and called you to help
him recover his files. The next day, you go to Bart's house and
analyze the situation: as you thought, the ransomware is the infamous
Burl1(ONE), which encrypts PC files by storing the encryption key
inside images with the .png extension, turning them into intricate
puzzles. Because Bart stores his images on an on cloud service, you
manage to retrieve the original images so you can reconstruct the
ransomware's encryption key and decrypt all his precious files. Will
you be able to find all the keys and recover all the files?
Bart is counting on you!

The Burl1 ransomware stores the encryption key by dividing images with
the .png extension into square tiles and performing or not performing
rotations of the individual tiles of 90, 180 or 270°, that is,
performing one, two or three rotations to the right. The key will
respectively have an 'R' (right) an 'F' (flip) or an 'L' (left),
depending on the rotation made. The absence of rotation reports the
character 'N'.

For each image, it is necessary to reconstruct the encryption key in
the form of a list of strings: each string corresponds to the sequence
of rotations of each tile in a row. So a 100x60 image in which the
tiles are size 20 will hide an encryption key of 15 characters,
organized into three strings of five characters each. In fact, there
will be 5 tiles per row (100//20 = 5) and 3 rows (60//20 = 3). To find
out the rotations performed you have to use the image you retrieved
from the cloud to compare with the encrypted image.

You need to write the function
jigsaw(puzzle_image:str, plain_image:str, tile_size:int, encrypted_file:str, plain_file:str) -> list[str]
that takes as input:
 - the name of the file containing the image with the rotated tiles,
 - the name of the file containing the image with the unrotated tiles,
 - an integer indicating the size of the side of the square tiles, 
 - the name of a text file to be decrypted with the encryption key, and
 - the name in which to save the decrypted file.

The function must reconstruct and return the encryption key hidden in
the image in puzzle_image and use it to decrypt the encrypted file,
saving the plaintext in a file called plain_file. The key is the
sequence of rotations to be made to reconstruct the initial image and
decrypt the input file.

For example, comparing the image in test01_in.png with test01_exp.png
and considering the 20-pixel square tiles, it can be determined that
the rotations applied were
  - 'LFR' for the tiles in the first row,
  - 'NFF' for the tiles in the second row, and
  - 'FNR' for the tiles in the third row.
So the key to be returned will be: ['LFR', 'NFF', 'FNR'].

Decryption of the file is achieved by implementing a transformation
depending on the character of the key in position i, modulo the length of the
key.  For example, if the key is ['LFR', 'NFF', 'FNR'], the key is 9
long, and we need to decrypt the character at position 14 of the input
file, we need to consider the character at position 14%9 = 5 of the
key, i.e., 'F'.
The transformations for decryption are as follows:

  - R = text[i] replaced by the character with following ord
  - L = text[i] replaced by the character with previous ord
  - N = remains unchanged
  - F = swap text[i] with text[i+1]. If i+1 does not exist, we consider
        the character text[0].

For example, if the key is LFR and the ecrypted text is BNVDCAP, the
plaintext will be AVOCADO since the decryption will be the following:

step     key      deciphering-buffer
1        LFR      BNVDCAP -> ANVDCAP
         ^        ^
2        LFR      ANVDCAP -> AVNDCAP
          ^        ^
3        LFR      AVNDCAP -> AVODCAP
           ^        ^
4        LFR      AVODCAP -> AVOCCAP
         ^           ^
5        LFR      AVOCCAP -> AVOCACP
          ^           ^
6        LFR      AVOCACP -> AVOCADP
           ^           ^
7        LFR      AVOCADP -> AVOCADO
         ^              ^

'''

# %%
import images


def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    pass

if __name__ == '__main__':
    print(jigsaw('tests/test01_in.png', 'tests/test01_exp.png', 20,
                                    'tests/test01_enc.txt', 'output/test01_out.txt'))

