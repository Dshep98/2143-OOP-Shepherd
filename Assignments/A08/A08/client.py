"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests

r = requests.post('http://localhost:8888/public_key/key.public.pem')

print(r.text)

