import pyqrcode

def print_QR(string):
    qr = pyqrcode.create(string, version = 1)
    print(qr.terminal(quiet_zone=1))
    
