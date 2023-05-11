#this code is meant to write the UID on the RFID card and the sensing is taking place using the MFRC522 RFID reader
#this will be carried out on a Raspberry Pi 3B+ with a MFRC522 RFID reader
#Write this code using Python 3

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

#capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading #global variable to stop the loop
    print("Ctrl+C captured, ending read.") #print to console
    continue_reading = False #set the global variable to false
    GPIO.cleanup() #cleanup the GPIO
    
#Hook the SIGINT
signal.signal(signal.SIGINT, end_read) #when Ctrl+C is pressed, call the end_read function

#Create an object of the class MFRC522
Reader = MFRC522.MFRC522() #this is the RFID reader

while continue_reading:
    #Scan for cards
    (status,TagType) = Reader.MFRC522_Request(Reader.PICC_REQIDL) 
    
    #If a card is found
    if status == Reader.MI_OK:
        print("Card detected") 
        
    #Get the UID of the card
    (status,uid) = Reader.MFRC522_Anticoll()
    
    #If we have the UID, continue
    if status == Reader.MI_OK:
        #Print UID
        print("Card read UID: %s,%s,%s,%s" % (uid[0],uid[1],uid[2],uid[3]))
        
        #This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        #Select the scanned tag
        Reader.MFRC522_SelectTag(uid)
        
        #Authenticate
        status = Reader.MFRC522_Auth(Reader.PICC_AUTHENT1A, 8, key, uid)
        
        #Check if authenticated
        if status == Reader.MI_OK:
            #Write the UID to the card
            Reader.MFRC522_Write(8, uid)
            Reader.MFRC522_StopCrypto1()
        else:
            print("Authentication error")  