# coding=utf8
#Author: Xose
#port to python3

#IMPORTS

import adb_library
from PIL import Image
#import wincmd
#import Tkinter
#import tkFileDialog
import os
import time
from datetime import datetime
import sys
from tkinter import ttk
from tkinter import *
#from Tkinter import *
#import tkMessageBox
#import Tkinter

#FUNCTIONS

def about_program():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("about")  # Titulo de la ventana
    root.iconbitmap('main_ico.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=31, height=3, padx=5, pady=5)
    texto.insert(tk.END,"ANDROID TOOL\nAuthor: Xosé Brais Noya García\nhttps://github.com/xoseng\n")
    texto.config(state="disabled")
    root.mainloop()

def license_agreement():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("license agreement")  # Titulo de la ventana
    root.iconbitmap('main_ico.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=77, height=8, padx=5, pady=5)
    texto.insert(tk.END,"GNU General Public License v3.0\n\n"
                        "Permissions of this strong copyleft license are conditioned\n"
                        "on making available complete source code of licensed works and modifications,\n"
                        "which include larger works using a licensed work, under the same license.\n"
                        "Copyright and license notices must be preserved.\n"
                        "Contributors provide an express grant of patent rights.\n")
    texto.config(state="disabled")
    root.mainloop()


def howto_start():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("how to start")  # Titulo de la ventana
    root.iconbitmap('main_ico.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=81, height=17, padx=5, pady=5)
    texto.insert(tk.END,"MANUAL - STEPS TO USE ANDROID TOOL\n\n"
                        "1 - ADB-TOOLS REQUIRED\n"
                        "If you don't have it, download here:\n"
                        "https://forum.xda-developers.com/attachment.php?attachmentid=4623157&d=1540039037\n\n"
                        "2 - ENGINEERING MODE REQUIRED\n"
                        "Settings > About Phone > Build Number > Now tap the build number a few times!\n\n"
                        "3 - SET USB DEBUGGING ON\n"
                        "Settings > Engineering Mode > USB debugging\n\n"
                        "4 - CONNECT ANDROID PHONE TO COMPUTER VIA USB\n\n"
                        "5 - START PROGRAM WITH CONNECT BUTTON\n"
                        "If it works it should show 'CONNECTED'")
    texto.config(state="disabled")
    root.mainloop()

def faq():
    #import Tkinter as tk
    import tkinter as tk
    root = tk.Tk()
    root.title("FAQ")  # Titulo de la ventana
    root.iconbitmap('main_ico.ico')  # Icono de la ventana, en ico o xbm en Linux
    root.resizable(0, 0)
    texto = tk.Text(root)
    texto.pack()
    texto.config(width=85, height=8, padx=5, pady=5)
    texto.insert(tk.END,"FAQ - ABOUT ANDROID TOOL\n\n"
                        "1 - ANDROID TOOL has been developed for Android versions 4.4+\n"
                        "2 - It's possible get results of the log file if they do not appear in the main boxes\n"
                        "3 - Factory reset ONLY WORKS in root devices\n"
                        "4 - ENGINEERING MODE REQUIRED\n"
                        "5 - USB DEBUGGING ON REQUIRED")
    texto.config(state="disabled")
    root.mainloop()

def exit_program():
        exit(0)

def connection_status():
    #debería de limpiar todas las variables, no sólo la que sobreescribe
    connect_val.set("")
    imei_val.set("")
    serial_val.set("")
    version_val.set("")
    model_val.set("")
    androidversion_val.set("")
    manufacturer_val.set("")
    macwiffi_val.set("")
    macbt_val.set("")
    #adb_library.adb_start()

    status=adb_library.device_status()
    connect_val.set(status)

    if status == 'CONNECTED':
        imei=adb_library.get_imei()
        imei_val.set(imei)
        serial=adb_library.get_serial()
        serial_val.set(serial)
        version=adb_library.get_version()
        version_val.set(version)
        model=adb_library.get_model()
        model_val.set(model)
        androidv=adb_library.get_androidversion()
        androidversion_val.set(androidv)
        manufacturer=adb_library.get_manufacturer()
        manufacturer_val.set(manufacturer)
        macwiffi=adb_library.get_macwiffi()
        macwiffi_val.set(macwiffi)
        macbt=adb_library.get_macbt()
        macbt_val.set(macbt)

def make_call():
    number=makecall_val.get()
    if number !='':
        adb_library.make_call(number)

def end_call():
    adb_library.end_call()

def save_log():
    from tkinter import filedialog
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    try:
        text2save = adb_library.get_info()
        f.write(text2save)
        f.close()
    except:
        f.close()

def reset_device():
    adb_library.factory_reset()

#MAIN GUI

root = Tk()
root.config(bd=30)
root.title("ANDROID TOOL")     # Titulo de la ventana
root.iconbitmap('main_ico.ico')  # Icono de la ventana, en ico o xbm en Linux
root.resizable(0, 0)         # Desactivar redimension de ventana

menubar = Menu(root)
root.config(menu=menubar)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Info")
helpmenu.add_separator()
helpmenu.add_command(label="How to start", command=howto_start)
helpmenu.add_command(label="License agreement", command=license_agreement)
helpmenu.add_command(label="FAQ", command=faq)
helpmenu.add_command(label="About", command=about_program)
helpmenu.add_command(label="Exit", command=exit_program)
menubar.add_cascade(label="Info", menu=helpmenu)

#imagen = PhotoImage(file="simple_logo.gif")
#Label(root, image=imagen).pack(side="top")

##########################GLOBAL TK VARS DECLARATION

connect_val = StringVar()
makecall_val= StringVar()
imei_val=StringVar()
serial_val=StringVar()
version_val=StringVar()
model_val=StringVar()
androidversion_val=StringVar()
manufacturer_val=StringVar()
macwiffi_val=StringVar()
macbt_val=StringVar()
####################################################

#root.geometry("400x400")
connect_button=Button(root, justify="left", text="CONNECT", command=connection_status).grid(row=0, column=0, padx=5, pady=2)
connect_value=Entry(root, justify="center", textvariable=connect_val, state="disabled", width=25).grid(row=0, column=1, padx=5, pady=2)

call_button=Button(root, text="MAKE CALL", command=make_call).grid(row=3, column=0, padx=5, pady=2)
call_value=Entry(root, justify="center", textvariable=makecall_val, state="normal", width=25).grid(row=3, column=1, padx=5, pady=2)
hangup_button=Button(root, text="HANG UP", command=end_call).grid(row=3, column=2, padx=5, pady=2)

imei_label=Label(root, justify="center", text="IMEI", state="normal").grid(row=4, column=0, padx=5, pady=2)
imei_value=Entry(root, justify="center", textvariable=imei_val, state="disabled", width=25).grid(row=4, column=1, padx=5, pady=2)

serial_label=Label(root, justify="center", text="SERIAL", state="normal").grid(row=5, column=0, padx=5, pady=2)
serial_value=Entry(root, justify="center", textvariable=serial_val, state="disabled", width=25).grid(row=5, column=1, padx=5, pady=2)

androidversion_label=Label(root, justify="center", text="ANDROID", state="normal").grid(row=6, column=0, padx=5, pady=2)
androidversion_value=Entry(root, justify="center", textvariable=androidversion_val, state="disabled", width=25).grid(row=6, column=1, padx=5, pady=2)

version_label=Label(root, justify="center", text="VERSION", state="normal").grid(row=7, column=0, padx=5, pady=2)
version_value=Entry(root, justify="center", textvariable=version_val, state="disabled", width=25).grid(row=7, column=1, padx=5, pady=2)

model_label=Label(root, justify="center", text="MODEL", state="normal").grid(row=8, column=0, padx=5, pady=2)
model_value=Entry(root, justify="center", textvariable=model_val, state="disabled", width=25).grid(row=8, column=1, padx=5, pady=2)

manufacturer_label=Label(root, justify="center", text="MANUFACTURER", state="normal").grid(row=9, column=0, padx=5, pady=2)
manufacturer_value=Entry(root, justify="center", textvariable=manufacturer_val, state="disabled", width=25).grid(row=9, column=1, padx=5, pady=2)

macwiffi_label=Label(root, justify="center", text="MAC WIRELESS", state="normal").grid(row=10, column=0, padx=5, pady=2)
macwiffi_value=Entry(root, justify="center", textvariable=macwiffi_val, state="disabled", width=25).grid(row=10, column=1, padx=5, pady=2)

macbt_label=Label(root, justify="center", text="MAC BLUETOOTH", state="normal").grid(row=11, column=0, padx=5, pady=2)
macbt_value=Entry(root, justify="center", textvariable=macbt_val, state="disabled", width=25).grid(row=11, column=1, padx=5, pady=2)

resetdevice_button=Button(root, text="FACTORY RESET DEVICE", command=reset_device).grid(row=13, column=1, padx=5, pady=2)

saveinfo_button=Button(root, text="SAVE LOG INFO", command=save_log).grid(row=14, column=1, padx=5, pady=2)

# Finalmente bucle de la aplicacion
root.mainloop()

