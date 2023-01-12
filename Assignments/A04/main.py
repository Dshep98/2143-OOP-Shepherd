import pprint as pp
import sys
from build_polybius import AdfgxLookup
from collections import OrderedDict
import math

#print("THIS IS A TEST TO SEE IF IT WORKS:")
B = AdfgxLookup('helloworldhowareyou')

# build my lookup table 
lookup = B.build_polybius_lookup()

# print out the actual matrix I 
# know I'm not insane!
#B.sanity_check()

#print("THIS IS THE TABLE FOR B:")
# print out my adfgx lookup table
#pp.pprint(lookup)

#print("THIS IS THE ENCRYPTION FOR MESSAGE: ")
message = "theattackisatdawn"
#for x in message:
  #print(lookup[x],end=' ')

print("\n\nStart of Program")
#keyword 1: fail
#keyword 2: grade
A=AdfgxLookup('quark')
lookup=A.build_polybius_lookup()
A.sanity_check()
print("THIS IS THE LOOKUP TABLE FOR A:")
# print out adfgx lookup table
pp.pprint(lookup)

print("THIS IS THE ENCRYPTION FOR MESSAGE: ")
message = "codenamethecleaner"
for x in message:
  print(lookup[x],end=' ')
###########################################
## Not sure if this is entirely correct but its storing the encrypted message into the columns
result=''
for x in message:
  result= result + lookup[x]
  message=result

##########################################
print('\n\n')
##Prints out matrix
def print_matrix(matrix,rows):
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")

def print_message(matrix,keyword):
    """ Prints the message in a left to right fashion, but reads it from
        the matrix by using fractionated matrix. If you think about it
        we don't even need to swap the columns around, if we alphabatize
        the keyword, then use the alphabetized letters to access the 
        matrix. 
    """
    i = 1 
    print(key1, ' :')
    for k in sorted(keyword):
        for d in matrix[k]:

            print(d,end='')

            # the spaces between every two letters is only for appearance
           
            if i % 2 == 0:
                print(' ',end='')
            i += 1
    print("")

def get_message(matrix,key2word):
    """ Prints the message in a left to right fashion, but reads it from
        the matrix by using fractionated matrix. If you think about it
        we don't even need to swap the columns around, if we alphabatize
        the key2word, then use the alphabetized letters to access the 
        matrix. 
    """
    message = ''
    i = 1
    for k in sorted(key2word):
        for d in matrix[k]:

            message += d
            i += 1
    return message
##########################################################
key1 = "quark".upper()

key_length = len(key1)
message_length = len(message)

rows = math.ceil(float(message_length)/float(key_length))
short_cols = key_length - (message_length%key_length)

matrix = {}

for k in key1:
    matrix[k] = []

i = 0
for m in message:
    matrix[key1[i]].append(m)
    i += 1
    i = i % len(key1)

#print_matrix(matrix,rows)

temp_matrix = sorted(matrix.items())

sorted_matrix = {}

for item in temp_matrix:
   sorted_matrix[item[0]] = item[1]

print_matrix(sorted_matrix,rows)

# Print the message using the sorted unnecessary matrix
print_message(sorted_matrix,key1)
#################################################################################################################################################################################
### Prints the columns from encrypted cipher text
key1_sorted = sorted(key1)
#### Prints number of each matrix
encrypted = get_message(matrix,key1)
for i in range(len(encrypted)):
    if i < 10:
        e = "  "
    else:
        e = " "
    print(i,end=e)
print("")
##prints letters in cipher indivisually
for i in range(len(encrypted)):
    print(encrypted[i],end="  ")
print("")
key_length=len(key1)

print("Length of cipher:",message_length)
print("Key Length: ", key_length)
#prints the length of roads and columns
long_rows = math.ceil(float(message_length)/float(key_length))
short_rows= math.ceil(float(message_length)/float(key_length)-1)
short_cols = key_length - (message_length%key_length)
cols = len(key1)

print(f"Long rows: {long_rows}")
print(f"Short rows: {short_rows}")
print(f"cols: {cols}")
print(f"short cols: {short_cols}")

print("\n")

tracker = {}         
for i in range(len(key1)):
  if rows == long_rows:
    tracker[key1[i]]=long_rows
    ##Somethigs wrong its never being read
  elif rows==short_rows:
   tracker[key1[i]] = short_rows
   
##its still off or in correct
print(tracker)

## Hard coded each slice indivisually becuase i dont know how to loop it
s1=(encrypted[:8])
print(s1)
s2=(encrypted[8:14])
print(s2)
s3=(encrypted[14:21])
print(s3)
s4=(encrypted[21:28])
print(s4)
s5=(encrypted[28:35])
print(s5)
print('\n')
###prints the maxtrix
i = 0
for k in encrypted:
    matrix[key1[i]].append(k)

print_matrix(sorted_matrix,rows)



  
print("")

#HAS TO BE RAN WHEN WE HAVE THE MATRIX FORMED
B = AdfgxLookup(matrix)
lookup=B.build_polybius_lookup()
pp.pprint(lookup)
############################################################
############################################################
#FOR THIS PART I DIDNT BOTHER TO DO EVERYTHING LIKE i DID WITH KEYWORD 1
#IT JUST STOPS AFTER ITS ENCRPYTED FROM THE ADFGX TABLE
#######################################################################
print('\n\n\n')
##Prints out matrix
def print_matrix(matrix,rows):
    for k in matrix:
        print(k,end=' ')
    print("")
    for k in matrix:
        print('-',end=' ')

    print("")
    for r in range(rows):
        for k in matrix:
            if r < len(matrix[k]):
                print(matrix[k][r],end=" ")
            else:
                print(" ",end=' ')
        print("")
def print_message(matrix,keyword):
    """ Prints the message in a left to right fashion, but reads it from
        the matrix by using fractionated matrix. If you think about it
        we don't even need to swap the columns around, if we alphabatize
        the keyword, then use the alphabetized letters to access the 
        matrix. 
    """
    i = 1 
    print(key2, ' :')
    for k in sorted(keyword):
        for d in matrix[k]:

            print(d,end='')

            # the spaces between every two letters is only for appearance
           
            if i % 2 == 0:
                print(' ',end='')
            i += 1
    print("")



key2 = "shine".upper()

#message= message.replace(' ','')

key_length = len(key2)
message_length = len(message)

rows = math.ceil(float(message_length)/float(key_length))
short_cols = key_length - (message_length%key_length)

matrix = {}

for k in key2:
    matrix[k] = []

i = 0
for m in message:
    matrix[key2[i]].append(m)
    i += 1
    i = i % len(key2)

#print_matrix(matrix,rows)

temp_matrix = sorted(matrix.items())

sorted_matrix = {}

for item in temp_matrix:
   sorted_matrix[item[0]] = item[1]

print_matrix(sorted_matrix,rows)
# Print the message using the sorted unnecessary matrix
print_message(sorted_matrix,key2)
