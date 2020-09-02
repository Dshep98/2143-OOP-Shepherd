import sys
import os

alphabet = [chr(x+97) for x in range(26)]
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
    opencipher=open("ciphertext1.txt", "r")
    ciphertext1= opencipher.read()
    print("Downloading Text ...")
    opencipher2=open("ciphertext2.txt", "r")
    ciphertext2= opencipher2.read()
    print("Calculating frequency...")
    F = Frequency()
   
    F.count(ciphertext1)
    F.print()
