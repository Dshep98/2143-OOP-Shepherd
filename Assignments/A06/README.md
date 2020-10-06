## Assignment 6: Prime Factor
### Dominique Shepherd

### Description: This program reads in numbers from a file to determine if their prime or not. If a number is prime the program should print prime and if not print the factors of the number.

### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [get_factors.cpp](./get_factors.cpp)     | solution file with everything in it.                         |
|   2   | [num.txt](./num.txt)|Big number input file  |
|   3   | [input.dat](./input.dat)| small number input file      |
|   4   | [output.txt](./output.txt)| holds the output produced from both the small number and big number files      |


### Instructions

- This project was compiled using repl.it's c++
- I am not sure if its safe to be ran anywhere else.
- the file I used for the program submitted was the [num.txt](./num.txt) which holds the big numbers. 
### Sources
- I used this video to touch up and logically understand what Prime and composit numbers are
https://www.youtube.com/watch?v=FBbHzy7v2Kg
https://www.youtube.com/watch?v=3h4UK62Qrbo
 - this video helped to understand and clear up the code I was writing
 https://www.youtube.com/watch?v=OLfVDBmZ3Xg
 - When I had trouble figuring out how to print all the factors out I watched this video and figured out thats when I need to change "num" to "i".
https://www.youtube.com/watch?v=rmD2VRwOgRs
- Dr.Griffin provided a sample input file and suggested I fix the prime problem by creating a seprate function that returns true or false to main.
### Problems
- Figuring out the factors once the prime numbers were found was a problem, because I'd get it to print one of the factors
  initally but nothing else would print. So then I switched it to print just "i" instead of "num".
  
 - Once I combined the code for primes and composites there was a problem with the primes. As shown below
- Number 1: 2-Factors:  Prime,,
  Number 2: 3-Factors:  Prime,,
  Number 3: 4-Factors:  2,   ,,
  Number 4: 5-Factors:       ,,
  Number 5: 6-Factors:  2, 3,,,
  Number 6: 7-Factors: 

- Its printing the factors of the numbers that are not prime and the first two primes but not the rest like for number 4 & 6.
