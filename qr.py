import pyqrcode

def print_QR(string):
    qr = pyqrcode.create(string)
    print(qr.terminal(quiet_zone=1))
    
