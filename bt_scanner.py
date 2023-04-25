import subprocess
from sys import stdout

def get_nearby_devices():
    output = subprocess.run(["hcitool", "scan"], capture_output=True)
    command_output = output.stdout.decode(stdout.encoding)
    command_output = command_output.replace("Scanning ...\n", "")
    # command_output = command_output.replace("\t", " ")
    return command_output

if __name__ == "__main__":
    print("Running hcitool")
    output = get_nearby_devices()
    print("Finished running hcitool. Output:")
    print(output)
