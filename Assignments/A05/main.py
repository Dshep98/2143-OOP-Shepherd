import sys
import dict
import frequency 
import sys
import os
import pprint


with open("dict","r") as f:
  word=f.readlines()

for i in range(len(word)):
  word[i]=word[i].strip()

if "cutthroat" in word:
  print("exist")
else:
  print("nope")


sys.exit

####################################################################################################################################################################################
#Run a frequency analysisfor cipher text

alphabet = [chr(x+97) for x in range(26)]
typical_frequency = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
}


class Frequency():
  def __init__(self):
      self.text = ""
      self.freq = {}
      self.sort_freq = None

      for l in alphabet:
          self.freq[l] = 0
  
  def count(self,text):
      for l in text:
          l = l.lower()
          if l in alphabet:
              self.freq[l] += 1

      #https://realpython.com/python-lambda/
      self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

  def print(self):
      if self.sort_freq:
          for f in self.sort_freq:
              print(f"{f[0]}:{f[1]}")
      else:
          print(self.freq)

  def getNth(self,n):
      if self.sort_freq:
          return self.sort_freq[n][0]

      return None



if __name__=='__main__':
    opencipher=open("ciphertext", "r")
    ciphertext1= opencipher.read()  
    print("Calculating frequency...")
    F = Frequency()
    F.count(ciphertext1)
    F.print()
    
    


###################################################################################################################################################################################
##STARTING WITH I.C- To find Key length

#First find the length of the text for 'N'
message=open("plaintext","r")
Text=message.read()
Text= Text.replace(' ','')   # get rid of spaces

N=len(Text) # length of text
c=26 #For the number of letters in the alphabet im assuming
# Second find the frequency of each letter for n_i
n_i='' #frequency of each letter # unsure of how to apply frequencies here


####Has to be fixed
#print(typical_frequency[0])
#used to find the I.c for the vigenere text
for i in range(26):
  result=(typical_frequency[i]-Frequency[i]**2)
  print(result,end="")




