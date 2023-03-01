import time
import pyperclip
import os
clear = lambda: os.system('cls')
clear()
class Track2to1:
    print("Coded by Kr1ptonn")
    print("Educational purposes only!")
    print("github.com/Kr1ptonn")
    time.sleep(1)
    while True:
        pan = input("\nEnter your PAN (CCN): ")
        if (len(pan) == 16):
            pass
        else:
            print("You typed more or less digits than 16! Try Again.")
            time.sleep(2)
            continue
        if (pan[0] == "4" or pan[0] == "5"):
            pass
        else:
            print("This script is only coded for VISA/MASTERCARD only!")
            time.sleep(1)
            continue
        track2 = input("Enter the second part: ")
        servicecode = track2[4] + track2[5] + track2[6]
        trackfix = track2.removeprefix(track2[0:7])
########- All of this script is only coded for educational purposes only!
########- I do not encourage/be part of any illegal activity!
########- This script is based onto google legal searches about how this works.
        bank = "B"
        bank += pan
        cardholder_fname = input("Enter CardHolder First Name (Leave blank if none): ")
        cardholder_lname = input("Enter CardHolder Last Name (Leave blank if none): ")
        card_expiry = input("Enter Card Expiry date (Format: YYMM): ")
        service10 = "0000000000"
        service6 = "000000"
        final_track = f'{bank}^{cardholder_lname.upper()}/{cardholder_fname.upper()}^{card_expiry}{servicecode}{service10}{trackfix}{service6}'
        print('\nSUCCESS! Wait for Output...')
        time.sleep(2)
        print(final_track)
        time.sleep(1)
        print('\nTrack 1 already copied into the clipboard!')
        pyperclip.copy(final_track)
        time.sleep(1)
        cont = input("\nIf u want to try again press (Y): ")
        if cont.upper() == "Y":
            clear()
            continue
        else:
            print('Bye!')
            time.sleep(1)
            exit()
