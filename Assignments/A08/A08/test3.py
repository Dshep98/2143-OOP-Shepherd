"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json
import sys
from crypto_class2 import Crypto
import cryptography
# Used to Generate Keys
# from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

#Used to Store Keys and Read in Keys
from cryptography.hazmat.primitives import serialization

#Used to do Encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding





TOKEN = '981d0c41ad0e128a0eace265d77bfcb3'
UID = '5749000'
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}
#######################################################################################################
###GRIFFINS FUNCTIONS
#########################################################################################################

def loadPubKey(pubkey):
    return serialization.load_pem_public_key(pubkey)

def pubKey():
    global PUBKEYS
    route = 'getPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        keys = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for key in keys['data']:
        PUBKEYS[key['uid']] = key

def getUsers():
    global USERS
    global PUBKEYS

    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        users = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for user in users['data']:
        if user['uid'] in PUBKEYS:
            user['pubkey'] = PUBKEYS[user['uid']]
            USERS[user['uid']] = user


###################################################################
def get_users():
    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    r = requests.get(url)

    data = r.json()

    with open("chat_users.txt","w") as f:
        f.write(json.dumps(data['data']))

    return data['data']

def get_user_with_id(id,users):
    for user in users:
        if user['uid'] == id:
            return user
        #print(user)

    return None       

#################################################################
def getActive():
    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = PUBKEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users



def postMessage(message,to_uid):
    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
       'uid':UID,
       'to_uid':to_uid,
       'message':message,
       'token':TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()

               
    
######################################################################################################
##MENU FUNCTIONS
#####################################################################################################

def postPubkey(PubKey):
    route = 'postPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.post(url)
    payload = {
       'uid':UID,
       'token':TOKEN,
       'pub_key': PubKey
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()



def getMessage(UID,count):
    route = 'getMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)
    payload = {
       'uid':UID,
       'token':TOKEN,
       'count': count
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers, json=payload)
    return r.json()

def sendMessage():
    ### Sends a message to specified user
    msg=input("Enter message to be sent::  ")
    to_Be_Sent=input("Enter the persons id you wish to send it to:  ")
    result = postMessage(msg,to_Be_Sent)
    #EncryptYourMessage(result)
    print (result)

def LookupUser():
    # Prints specific user asked for
    users=get_users()
    USERid=input("Enter user ID for person to be found::")
    user=get_user_with_id(USERid,users)
    print(user)
        

def recentlyActive():
    ### Prints recently active users
    active = getActive()
    for a in active:
        print(a)

def Allusers():
    ## Prints all users
    getUsers()
    print(USERS)

def CheckMsg():
    answer=input("Enter your userId to check your messages::  ")
    lastfew=input("Enter a number for the latest messages to be checked::: ")
    result=getMessage(answer,lastfew)
    print(result)


def Choices():
    choice = False
    while not choice:
        print("Options-")
        print("r- Recently active users")# Shows recently active people
        print("a - All users")## Each user diplays the , and public key
        print("l - look up specific user")# When it runs it only displays the first/last name, user ID, and email
        print("s - send a message to someone")
        print("c - check your own messages")
        print("q - Quit")
        choice = input("Enter option to proceed::  ")
        if choice == "r":
            recentlyActive()
        elif choice == "a":
            Allusers()
        elif choice == "l":
            LookupUser()
        elif choice == "s":
            sendMessage()
        elif choice == "c":
            CheckMsg()
        elif choice == "q":
            print("Adios Amigos!")
            choice = True
        else:
            print("Invalid Choice")
            print("Please try again")
       ##posibbly needs to be fixed as a continous loop
def Keys():
    SecretMessage = Crypto()
    SecretMessage.generate_keys()
    SecretMessage.get_storable_keys()
    SecretMessage.store_keys()
    SecretMessage.load_keys()
    #encrypted = SecretMessage.encrypt(result)

   # decrypted = SecretMessage.decrypt(encrypted)
    #print(encrypted)



if __name__ == '__main__':
   pubKey()
   getUsers()
   Choices()
    # msg=input("Enter message to be encrypted:::  ")
    # EncryptYourMessage(msg)
   
   response=postPubkey(Keys())
   print(response)
   
   

"""
    # A: Basic Start Of Workflow: 
    #     - Generate your own public and private key
    #     - Post your public key at beginning of session
    #     - Download everyones public keys so you can encrypt messages.
    # B: Encrypting a message: 
    #     - load target users public key and encode it using .encode('utf-8') (turns it into bytes)
    #     - encrypt the message to them with a string (also encoded utf8)
    #     - Important! See code snippets below.
    #         - base64 encode the encrypted message (base64 uses characters that we can put into json or strings)
    #         - then using your base64 encoded string, decode it AGAIN using .decode('utf8')
    #     - now you send your message using api
    # C: Decrypting messages:
    #     - get the message using the api.
    #     - decode the message using base64 decode
    #     - decrypt message 
    # System As a Whole:
    #     - Do step A
    #     - Look at active users
    #     - Send one of them a message using step B
    #     - Continuously check for messages from other users
    #     - Find one, get it and decrypt it.
    # """


#     # this is me loading a public key from my key dictionary
#     pk = loadPubKey(USERS['5147600']['pubkey'].encode('utf-8'))

#     # this encrypts the encoded plaintext mesage with a users public key
#     encrypted = pk.encrypt(
#         "This is a plaintext message encrypted with public key 5147600".encode('utf-8'),
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )
#     print(encrypted)

#     # For testing, I load same persons private key from a file
#     with open('./keys/5147600.private.key', "rb") as key_file:
#         private_key = serialization.load_pem_private_key(
#             key_file.read(),
#             password=None
#         )
#     # I decrypt message encoded with public key
#     original_message = private_key.decrypt(
#         encrypted,
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )

#     # print decrypted message
#     print(original_message)
#     encoded = base64.b64encode(encrypted)
#     result = postMessage(encoded.decode('utf8'),'8020')


#     # now get the message and decode it
#     route = 'getMessage'
#     url = f"{API}{route}&token={TOKEN}&uid={UID}&latest=true"
#     r = requests.get(url)
#     data = r.json()
#     message = data["data"][0]

#     #print messages (still encrypted)
#     print(message)

#     # turn it back into its original bytes form
#     decoded = base64.b64decode(message['message'])
#     print(decoded)

#     #should be decryptable now with right private key.
