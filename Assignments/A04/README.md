## Assignment 4: ADFGX Implementation
### Dominique Shepherd

#### FORE WARNING: This program is incomplete nothing is actually connected, everything is pretty much in one file & slightly organized, and its not set up to run from the command line in repl.it using the skeleton assigned. On the other side it runs but some things are correct and some aren't. Some things are just coded indivisually brute force because its the only way i could figure it out.
## I'd rather anyone not waste their time having go through all of it or if you want read through it at your own risk.

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
- Tons of help from professor griffin with the encrytion and fractionating process.

### Problems
- I faced pretty much alot of problems with this program especially the complexity of it and so many things to do with the code. However, the concept and topic of itself is pretty awesome reagardless of the complex code.
- Problem 1: Was undestanding how the lookup table came about.Yes, alot of helper code was given but actually using it and implementing it was still not understanding.
- Problem 2: Forming the message ing the ADFGX table. I made the message but initally I couldn't figure out how to hide it within the encrytion but I later figured that out. Not sure how I did I was kind of just bouncing thoughts around.(Its commented as : 
  Not sure if this is entirely correct but its storing the encrypted message into the columns
  result=''
  for x in message:
  result= result + lookup[x]
  message=result

  Its probaly the only piece of code I actually came up with in the entirety of the program. Oh well im proud of it!
- Problem 3: After that was the decrytion process. The whole process was said to done and reverse and was stated by professor griffinn and the sources i used as easy but  the code was just not coming to me. The concept process of it was easy to understand but not the coding. When I did understand sometimes I could figure out one part but not the rest which was frustrating in itself so I brute forced the code but that still didnt make it better.
- Honestly the whole complexity of this program was frustrating, interesting at times ,and mind boggling. The CODING IS DRIVING ME NUTS BECUASE NOTHING CLICKS AND CONNECTS LIKE I NEED IT TOO. But Its being turnt in anyway, because im not sure what else to do.
