import hashlib


def hashUID(uid, rolls=1):
	if rolls <= 0:
		return uid
	
	hashed = hashlib.sha256(uid.encode('utf-8')).hexdigest()

	return hashUID(hashed, rolls - 1)
