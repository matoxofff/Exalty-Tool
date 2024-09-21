import time
from colorama import Fore
from fade import *

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(line)
        time.sleep(delay)

instruction = """
1. Choose a Virtualization Software

You’ll need a hypervisor to create and manage VMs. The two most popular options are:

VirtualBox (Free, open-source)
VMware Workstation Player (Free for personal use)
Download and install your preferred software:

VirtualBox: https://www.virtualbox.org
VMware: https://www.vmware.com/

2. Download an ISO Image

An ISO file is a digital copy of an operating system. Choose the OS you want to install:

Ubuntu: Ubuntu Download
Windows: Windows ISO
Kali Linux (For Pen-testing): Kali Linux Download

3. Create a Virtual Machine

Open your virtualization software and follow these steps:

In VirtualBox:

Click on "New" to create a new VM.
Name your VM, select the operating system type (e.g., Linux, Windows), and allocate memory (RAM). A minimum of 2GB is recommended.
Create a virtual hard drive (VDI format, dynamic allocation is preferred).
Select the amount of storage space (minimum of 20GB recommended).

In VMware:

Click on "Create a New Virtual Machine".
Choose the installer disc image (ISO) and browse to the ISO you downloaded.
Follow the on-screen instructions to set up RAM, disk space, and other configurations.

4. Install the Operating System

Start the VM and it will boot from the ISO file.
Follow the standard installation steps for the chosen OS.
After installation, remove the ISO file from the virtual machine settings to avoid booting from it again.

5. Install Guest Additions / VMware Tools

Once the OS is installed, you can install Guest Additions (for VirtualBox) or VMware Tools (for VMware). These tools enhance performance, allow seamless mouse integration, enable shared clipboard functionality, and provide better display resolution.
In VirtualBox, go to Devices > Insert Guest Additions CD Image, then follow the prompts inside the VM.
In VMware, go to Player > Manage > Install VMware Tools.

6. Create Snapshots (Optional but Recommended)

Snapshots allow you to save the current state of your VM, so you can revert back if something goes wrong:

In VirtualBox, click on Snapshots and create a new snapshot.
In VMware, go to VM > Snapshot > Take Snapshot.

7. Testing in the Virtual Environment

Now that your VM is set up, you can use it to:

Test software.
Browse the web anonymously.
Perform ethical hacking in a safe environment (if using a specialized OS like Kali Linux).
Experiment with various configurations without affecting your main machine.

8. Security Tips

Always use a virtual network adapter to isolate the VM from your real network if testing potentially malicious software.
Regularly update the VM’s OS and take snapshots before any significant change.
Do not share files between the host machine and the VM unless you’re sure the files are safe."""


print(Fore.LIGHTRED_EX + "Instructions to install :")
print("")
print_with_delay(Fore.LIGHTBLACK_EX + instruction, delay=0.02)
print()
print(Fore.GREEN + f"I am in no way responsible for what you do")