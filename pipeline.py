from client import login, register
from qr import print_QR
UID = "1234567890"

# Register
url = register(UID)
print_QR(url)



