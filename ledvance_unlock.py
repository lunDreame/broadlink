"""Ledvance Unlock Script."""

import sys
import time

import broadlink as blk

def main():
    """Main function."""
    print(
        "Fisrt Step: \n"
        "1. Reset light by turning on and off 5 times \n"
        "2. Connect PC to light's AP 'LEDVANCE_Smart' \n"
    )
    time.sleep(1)
    user_input = input("Are you ready? Press Enter to continue...")
    if user_input != "":
        print("Wrong input, exiting...")
        sys.exit()
            
    ssid = input("Enter the your wifi SSID: ")
    password = input("Enter the your wifi password: ")
    if ssid != "" and password != "":
        print("Connecting to wifi...")
        blk.setup(ssid, password, 3)
        time.sleep(1)
        yes_or_no = input("PC network dropped from 'LEDVANCE_Smart' AP?, yes/no: ")
        if yes_or_no == "yes":
            yes_or_no = input("Is PC network connected back to regular WiFi SSID? yes/no: ")
            if yes_or_no == "yes":
                ip_address = input("Light ip address: ")
                device = blk.hello(ip_address)
                device.auth()
                device.set_lock(False)
                print("Unlock success!")
            else:
                print("Unexpected error, exiting...")
                sys.exit()
        else:
            print("Unexpected error, exiting...")
            sys.exit()
        
    
if __name__ == "__main__":
    main()