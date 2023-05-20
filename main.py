from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from qr import print_QR
from hashing import hashUID
from client import register, login, complete_registration, complete_login

### ALLOWED STATES ###
# LOGIN
# REGISTER
SYSTEM_STATE = "LOGIN"

reader = SimpleMFRC522()
def login_RFID():
    # GET UID
    (UID, _) = reader.read()
    print(UID)

    # On UID
    SUID = hashUID(str(UID), 50)

    # Login
    log = login(SUID)

    if log == False:
        return False
    
    OTP = input("ENTER OTP FROM AUTHENTICATOR: ")

    complete = complete_login(SUID, OTP)

    if complete == False:
        return False
    
    return True

def register_RFID():
     # GET UID
    (UID, _) = reader.read()
    print(UID)

    # On UID
    SUID = hashUID(str(UID), 50)

    # Register
    reg = register(SUID)

    if reg == False:
        return False

    print_QR(reg)
    # Complete Registration
    OTP = input("ENTER OTP FROM AUTHENTICATOR: ")
    reg_complete = complete_registration(SUID, OTP)
    return True

if SYSTEM_STATE == "LOGIN":
    complete = login_RFID()
    if complete:
        print("LOGIN SUCCESSFUL")
    else:
        print("LOGIN FAILED")

elif SYSTEM_STATE == "REGISTER":
    complete = register_RFID()
    if complete:
        print("REGISTRATION SUCCESSFUL")
    else:
        print("REGISTRATION FAILED")
else:
    print("INVALID STATE")


GPIO.cleanup()


