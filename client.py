import requests
import json
from hashing import hashUID

HASH_COUNT = 50

# URL
URL = "https://rfid-auth-server-production.up.railway.app"

def login(uid):
    # Hash the UID
		hashed = hashUID(uid, 50)

		# Send the request
		r = requests.post(URL + "/login", json={"uid": hashed})

		# Check the response
		if r.status_code == 200:
				return True
		else:
				return False
		
def register(uid):
		# Hash the UID
		hashed = hashUID(uid, 50)

		# Send the request
		r = requests.post(URL + "/register", json={"uid": hashed})

		# Check the response
		if r.status_code == 200:
				return True
		else:
				return False
		
print(login("test"))