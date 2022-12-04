from setuptools import setup, find_packages
import os
import sys
setup(
    name='SWTK',
    version='1.4.9',
    description='Sort txt file from weirdest line to last from cli. Meant to be used for Logs. An experimental Unsupervised Learning Log Anomaly Detection toolkit. YOU ARE BEAUTIFUL! This will sort the input based on weirdness',
    url='https://github.com/nileshkhetrapal/SWTK',
    author='Nilesh Khetrapal',
    packages=find_packages(),
    scripts=['bin/SWTK'],
)

if sys.platform == 'win32':
    print("Windows detected, this is not the recommended method of installation for this package on Windows. Please go to the SWTK github page and download the latest release from there.")
    #Get username
    username = os.getlogin()
    TriePath = 'C:\\Users\\' + username + '\\AppData\\Local\\Temp\\Trie.exe'
    # Check if anomaly_detection.exe is in the temp directory
    # If anomaly_detection.exe is not in the temp directory, download it from the repository,compile it and place it in the temp directory
    if not os.path.isfile("C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Trie.exe"):
        print("Trie.exe is not in the temp directory. Downloading it from the repository...")
        #Move trie.exe to the temp directory
        os.system("move Temp/trie.exe" + " C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Trie.exe")
        print("Trie.exe was downloaded successfully.")
        print("Moving Trie.exe to the temp directory...")
        print("Done.")
# If the host is linux or mac, check if the rust program is accessible

else:
    #Get the username
    #use popen to get the username
    username = os.popen("whoami").read()
    homedir = os.getenv("HOME")
    # TriePath has the location of the rust program
    #Create a string with the path to the rust program
    #Trie = str("/.local/bin/trie")
    #TriePath = homedir + Trie
    TriePath = "/bin/trie"
    #TriePath should point to the rust program in the usr/bin directory
    #TriePath = '/home/' + username + '/.local/bin/trie'
    # Check if the rust program is accessible

    if not os.path.isfile(TriePath):
        #move the trie program to the usr/bin directory
        print("Trie is being moved to the /bin directory...")
        os.system("sudo mv bin/trie /bin/trie")
        print("Done.")
        #make the trie program executable and move it to the /bin directory
        os.system("chmod +x " + TriePath)
        print("If you still have an error saying that anomaly dict is empty, you will likely have to recompile the rust program. Please go to the SWTK github page and download the latest release from there.")
