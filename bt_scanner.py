# Bluetooth scanner!
# To use: import bt_scanner.
# When the user selects the "Bluetooth Scanner" option in
#   the menu, just call bt_scanner.bt_scanner_gui().
# This function will return once the user clicks the X button.

import subprocess
from sys import stdout
import tkinter as tk

def bt_scanner_gui():
    root = tk.Tk()
    root.title("Bluetooth Scanner")
    root.geometry("500x300")

    # init label
    label = tk.Label(root, text="Scanning nearby Bluetooth devices.\nThis takes about 5 seconds.")    
    label.pack(expand=True)

    def update_with_scan():
        output = get_nearby_devices()
        to_display = "Detected devices:\n\n"
        for line in output.splitlines():
            line_parts = line.split("\t")
            to_display += "Name: " + line_parts[1] + "\n"
            to_display += "MAC: " + line_parts[0] + "\n\n"
        label.config(text=to_display)

    root.after(100, update_with_scan)
    root.mainloop()

def get_nearby_devices():
    output = subprocess.run(["hcitool", "scan"], capture_output=True)
    command_output = output.stdout.decode(stdout.encoding)
    command_output = command_output.replace("Scanning ...\n", "")
    command_output_split = command_output.splitlines()
    command_output_fixed = []
    for line in command_output_split:
        if line[0] == '\t':
            command_output_fixed.append(line[1:])
    
    return "\n".join(command_output_fixed)

if __name__ == "__main__":
    bt_scanner_gui()
