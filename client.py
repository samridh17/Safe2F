import requests
import json
from hashing import hashUID

HASH_COUNT = 50

# URL
URL = "https://rfid-auth-server-production.up.railway.app"
# URL = "http://localhost:3000"


def login(uid):
    # Hash the UID
    hashed = hashUID(uid, HASH_COUNT)

    # Send the request
    body = {"uid": hashed}

    headers = {"Content-Type": "application/json"}
    r = requests.post(URL + "/login", json=body, headers=headers)

    # Check the response
    response = json.loads(r.text)

    if r.status_code < 300:
        return response

    return False


def register(uid):
    # Hash the UID
    hashed = hashUID(uid, HASH_COUNT)

    # Send the request
    r = requests.post(URL + "/register", json={"uid": hashed})

    # Check the response
    if r.status_code < 300:
        response = r.json()
        url = response["totp"]

        return url
    else:
        return False

def complete_registration(uid, token):
		# Hash the UID
		hashed = hashUID(uid, HASH_COUNT)

		# Send the request
		r = requests.post(URL + "/register/complete", json={"uid": hashed, "totpCode": token})

		# Check the response
		if r.status_code < 300:
				return True
		else:
				return False
                
def complete_login(uid, token):
		# Hash the UID
		hashed = hashUID(uid, HASH_COUNT)

		# Send the request
		r = requests.post(URL + "/login/complete", json={"uid": hashed, "totpCode": token})

		# Check the response
		if r.status_code < 300:
				return True
		else:
				return False