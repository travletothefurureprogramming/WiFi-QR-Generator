import customtkinter as ctk
from tkinter import messagebox
from tkinter import filedialog
import qrcode
import datetime
from PIL import Image
import win32api
import win32print


password_showed = False


def generate_qr_code():
    size = size_dropdown.get()

    if size == "Small":
        box_size = 5
    elif size == "Medium":
        box_size = 10
    elif size == "Large":
        box_size = 20

    qr = qrcode.QRCode(
        version=1,
        box_size=box_size,
        border=4
    )
    
    ssid = ssid_entry.get()
    password = password_entry.get()
    security_type = security_type_dropdown.get()

    if security_type == "Open":
     wifi_string = f"WIFI:T:nopass;S:{ssid};;"
    else:
     wifi_string = f'WIFI:T:{security_type};S:{ssid};P:{password};;'

    qr.add_data(wifi_string)
    qr.make(fit=True)

    datetime_now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    directory_to_save = filedialog.askdirectory()

    filename = f"{directory_to_save}/wifi_qr_{datetime_now}.png"

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"\n✓ QR code saved as {filename}")
    messagebox.showinfo("QR code",f"✓ QR code saved as {filename}")
    

    with open("history.txt", "a") as f:
        f.write(f"{ssid}\n")

    img = Image.open(filename)
    
    preview_img = ctk.CTkImage(
        light_image=img,
        dark_image=img,
        size=(200, 200)
    )

    image_label.configure(image=preview_img)
    image_label.image = preview_img

    if do_you_want_to_print_check_box:
        win32api.ShellExecute(0, 'print', filename, f'/d:"{win32print.GetDefaultPrinter()}"', '.', 0)


def toogle_show_password():
   global password_showed

   if password_showed:
    password_entry.configure(show="*")
    password_showed = False
   else:
    password_entry.configure(show="")
    password_showed = True

app = ctk.CTk()
app.title("WiFi QR Generator")
app.geometry("600x600")

ssid_label = ctk.CTkLabel(app,text="SSID")
ssid_label.pack(pady=2)

ssid_entry = ctk.CTkEntry(app)
ssid_entry.pack(pady=2)

password_label = ctk.CTkLabel(app,text="PASSWORD")
password_label.pack(pady=2)

password_entry = ctk.CTkEntry(app,show="*")
password_entry.pack(pady=2)

show_check_box = ctk.CTkCheckBox(app,text="Show Password",command=toogle_show_password)
show_check_box.pack(pady=2)

security_label = ctk.CTkLabel(app,text="SECURITY TYPE")
security_label.pack(pady=2)

security_type_dropdown = ctk.CTkOptionMenu(app,values=["WPA","WPA2","WEP","Open"])
security_type_dropdown.pack(pady=2)

size_label = ctk.CTkLabel(app,text="SIZE")
size_label.pack(pady=2)

size_dropdown = ctk.CTkOptionMenu(app,values=["Small","Medium","Large"])
size_dropdown.pack(pady=2)

do_you_want_to_print_check_box = ctk.CTkCheckBox(app,text="Do you want to print the QR code")
do_you_want_to_print_check_box.pack(pady=2)

generate_btn = ctk.CTkButton(app,text="Generate",command=generate_qr_code)
generate_btn.pack(pady=2)

image_label = ctk.CTkLabel(app, text="")
image_label.pack(pady=10)


app.mainloop()