import time
import pyperclip
import os
clear = lambda: os.system('cls')
clear()
class Track2to1:
    while True:
        track2 = input("Track 2: ")
        if(track2[0] == "4" or track2[0] == "5"):
            pass
        else:
            print("This script is only coded for Visa/Mastercard")
            continue    
        card_name = input("Cardholder Name: ")
        card_last = input("Cardholder LastName: ")
        pin = input("Pin (If available): ")
        service10 = "0000000000"
        service6 = "000000"
        card_exp = track2[17:21]
        pan = track2[0:16]
        service_code = track2[21:24]
        fixed_track = track2.removeprefix(track2[0:24])
        final_track = f'B{pan}^{card_last.upper()}/{card_name.upper()}^{card_exp}{service_code}{service10}{fixed_track}{service6}^{pin}'
        print(final_track)
        pyperclip.copy(final_track)
        print("\nCopied!")
        ask = input("U want to start again? (Y/N): ")
        if ask.upper() == "Y":
            continue
        else:
            print("Bye")
            time.sleep(1)
            exit()
            
        
        