import sys
import dict
import sys
import os
import pprint
import Frequency

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

  def print(self, f):
      if self.sort_freq:
          for f in self.sort_freq:
              print(f"{f[0]}:{f[1]}")
      else:
          print(self.freq)

  def getNth(self,n):
      if self.sort_freq:
          return self.sort_freq[n][0]

      return None

#opens up the text to be read then counts the frequency of each letter
if __name__=='__main__':
    opencipher=open("ciphertext2", "r")
    ciphertext2 = opencipher.read()  
    F=Frequency()
    F.count(ciphertext2)
  ###################################################################
    # looks at every letter in the ciphertext and calculates the total IC and gives a score.
    total = 0
    for k,v in F.freq.items():
        #print(f"{k} , {v}")
        p = (v / len(ciphertext2)) # percentage of how often letter occurs in ciphertext
        #print(p,end=" ")
        sqdiff = ((typical_frequency[k]/100) - p)**2 # compare it to typical
        # total += float(v)/len(ciphertext2)
        #print(f"{k} , {sqdiff} , {p}, {v} ")
        total += sqdiff
    #print(f"Total: {total}") #Calculates the I.C of the ciphertext
    #in the end this will be compared to the indivisual I.C. from the key length that occurs at the highest percentage
    
    print("\n")
    ################################################################# 
    #find the I.C. of ciphtext then compare it to each sequence in the length
    ciphtxt = "tensw pez yqb xyimsg dmnv fhkz jbqn vgzb glmnmfwh"
    ciphtxt= ciphtxt.replace(' ','')   # get rid of spaces
    len_txt=len(ciphtxt)
    #print("LENGTH OF CIPHTXT:", len(ciphtxt))
    print("Calculating I.C....")
    F=Frequency()
    F.count(ciphtxt)
    #F.print()

    #p=percentage of how often letter occurs in text
    #k= the letter being read from text
    #v=how often the number appers

    total = 0 #keeps total of each indivisual frequency then adds them all together
    for k,v in F.freq.items():
      p = (v / len(ciphtxt)) # percentage of how often letter occurs in ciphertext
      #print(f"{k} , {p}, {v} ")
      sqdiff = ((typical_frequency[k]/100) - p)**2 # compare it to typical
      total += float(v)/len(ciphtxt)
      #print(f"{k} , {sqdiff} , {p}, {v} ")
      total += sqdiff
    print(f"Total or I.C.: {total}") #So the total is the original I.C. thats gonna get compared to the others
print('\n')
###################################################################
  #loop 14 times from 2-15 and keep going on up until 16
  #keep going unitl their is a posiblilty of their being two of a kind in terms of I.C that are the highest to evaluate with the original.
#ciphtxt = "tensw pez yqb xyimsg dmnv fhkz jbqn vgzb glmnmfwh"
#           2-2-2 -2- 2-2 -2-2-2 -2-2 -2-2 -2-2 -2-2 -2-2-2-2

for skip in range(2,5):
  #code you have to implement
  #I need to figure out how to cut the sequences into subsequences once it hits the end of the text for given length
  #then repeat for the next subsequence in that key length
  print('\n')
  print("If key were of length ", skip )
  print("\n")
  seq=1
  print("Sequence ",seq,": ")
  seq=seq+1
  # j = which letter to start on 
  for j in range(skip):
      # start at 0
      # then skip
      #2 at a time
        
      for i in range(j,len(ciphtxt),skip):
          if ciphtxt[i] in alphabet: 
              print(ciphtxt[i],end=" ")
              

 
