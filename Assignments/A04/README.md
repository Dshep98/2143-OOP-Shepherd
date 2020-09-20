## Assignment 4: ADFGX Implementation
### Dominique Shepherd
### Description:
- This program uses the ADFGX cipher to pass in two keywords. The first one is to buld the inital adfgx table the next then encrypt the table with a hidden message.
 - Then it has to reprint out encrytion doubled in size from the lookup table. So for the decryption we have to do the steps in reverse 1.Read out the columns in the unsorted matrix which is where the columnar transposition comes in at 2. Now you have the encrypted text, based off of the keyword you have to figure out the number of long rows & short rows,length of cipher text, and short colums & small columns 3.  seperate the letters in the cipher text the based of the length of the length of the rows then read it back into the maxrix column wise. 4. After the matrix is formed use the look up table to decipher the text to reaad out the hidden message.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [main.py](./main.py)     | solution file with everything in it.                         |
|   2   | [build_polybius.py](./build_polybius)| input file to help build the adfgx table         |



### Instructions

- This project was compiled using repl.it's python3
- I am not sure if its safe to be ran anywhere else.
### Sources
- This site was used to help me understand the concept better of using the columanr transposition cipher
https://crypto.interactive-maths.com/columnar-transposition-cipher.html
- This site was used to help me understand the slicing thing mentioned in class.
https://www.geeksforgeeks.org/string-slicing-in-python/
- I watched this to also help with the concept of undrstanding the encrption and decrytion process
https://www.bing.com/videos/search?q=from+a+columnar+transposition+how+to+read+off+columns&docid=608052362887695512&mid=5A85B655311B1DD75B975A85B655311B1DD75B97&view=detail&FORM=VIRE
- Professor griffin was also a big help with breaking down the fractionating process among other things.
