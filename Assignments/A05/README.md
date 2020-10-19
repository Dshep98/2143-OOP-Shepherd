## Assignment 5: Vigenere Cipher
### Dominique Shepherd

#### FORE WARNING: This program is incompleteand still in progress everything here is just what I have so far

### Description:
- This program uses the vigenere cipher, the files given are already encryted using this method. TO decrypt it you have to use a dictionary to find the length of the key
  and to narrow that process down you implent something called the incidence of coincidence, and that gives you an estimate of what the key length is. From there you run a frequency anaylisis and compare that with the incidence of coincidence to narrow down the length of the possible key in the dictionary. 

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [main.py](./main.py)     | solution file with everything in it.                         |
|   2   | [words.txt](./words)| dictionary used to find keyword        |
|   3   | [ciphertext](./ciphertext)| encrypted text       |


### Instructions

- This project was compiled using repl.it's python3
- I am not sure if its safe to be ran anywhere else.
### Sources
- This site was used to help me understand the concept better 
 http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-vigenere-cipher/
 http://practicalcryptography.com/cryptanalysis/text-characterisation/index-coincidence/
- Tons of help from professor griffin.

### Problems
- So after getting help with griffin for finding the incidence of coincendecne for the full text, I moved on to breaking the text down into subsequences based off of the key length from each time it ran. But the problem i've encountered is that I can get it to skip every other number its on with the key length but breaking it down into THe subsequence once its been ran is the problem. 
- Say for instance my lenth=2 its gonna print as this, which skips from the beginning every second other letter until the end.

# ciphtxt = "tensw pez yqb xyimsg dmnv fhkz jbqn vgzb glmnmfwh"
#            2-2-2 -2- 2-2 -2-2-2 -2-2 -2-2 -2-2 -2-2 -2-2-2-2

So once its run this is what I get:

If key were of length  2---
Sequence  1 :                             
t n w e y b y m g m v h z b n g b l n f h e s p z q x i s d n f k j q v z g m m w 
                                                      
- As shown its printing the sequence of the entirty of the text, but im unsure of cut of the text once its finish reading every other number for it to then shift to the next sequence in the text printing the numbers that it missed. Its supposed to break off into the next sequence after h but thats where I get stuck.
