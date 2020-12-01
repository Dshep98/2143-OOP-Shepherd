"""
https://requests.readthedocs.io/en/master/user/quickstart/

"""
import requests
msg=key.public.pem
file=open("key.public.pem","w")
file.write(msg)
print(msg)
file.close()

r = requests.post('http://localhost:8888/public_key',json={"key":msg})

print(r.text)

