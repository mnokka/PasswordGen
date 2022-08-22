
# idea from: https://stackoverflow.com/questions/3854692/generate-password-in-python
# mika.nokka1@gmail.com, 22.8.2022

# needed libs
#  pip install pyopenssl
#  pip install secrets


import secrets
import string
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(20))  # for a 20-character password
print ("Password:")
print (password)
