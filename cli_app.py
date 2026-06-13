import qrcode
from PIL import Image
import datetime
from getpass import getpass
import sys

security_types = ["WPA","WPA2","WEP","Open"]

try:
    with open("history.txt", "r") as f:
       pass
except FileNotFoundError:
    print("No history found.")
    with open("history.txt", "w") as f:
        f.write("")
    

def main_logic():

    ssid = input("Enter SSID: ")

    while not ssid.strip():
        print("SSID cannot be empty")
        ssid = input("Enter SSID: ")

    password = getpass("Enter password: ")
    security_type = input("Security Type (WPA/WPA2/WEP/Open): ")

    size = input(
    "\nSelect Size:\n"
    "1. Small\n"
    "2. Medium\n"
    "3. Large\n"
    "> "
    )

    if size == "1":
        box_size = 5
    elif size == "2":
        box_size = 10
    elif size == "3":
        box_size = 20
    else:
        box_size = 10

    qr = qrcode.QRCode(
        version=1,
        box_size=box_size,
        border=4
    )

    while security_type not in security_types:
        print("Please select a valid security type")
        security_type = input("Security Type (WPA/WPA2/WEP/Open): ")

    

    if security_type == "Open":
     wifi_string = f"WIFI:T:nopass;S:{ssid};;"
    else:
     wifi_string = f'WIFI:T:{security_type};S:{ssid};P:{password};;'

    qr.add_data(wifi_string)
    qr.make(fit=True)

    datetime_now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    filename = f"wifi_qr_{datetime_now}.png"

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"\n✓ QR code saved as {filename}")

    with open("history.txt", "a") as f:
        f.write(f"{ssid}\n")

    img = Image.open(filename)
    img.show() 




def main_menu():
    print("""
    ===================
     WiFi QR Generator
    ===================

    1. Generate QR
    2. View History
    3. Delete History
    4. Exit
          """)
    
    selection = input("Select: ")

    if selection == "1":
        main_logic()
    elif selection == "2":
     with open("history.txt", "r") as f:
        print(f.read())
    elif selection == "3":
     with open("history.txt", "w") as f:
        f.write("")
     print("✓ History deleted.")
    elif selection == "4":
       sys.exit()
    else:
       print("Invalid option")

while True:
   main_menu()