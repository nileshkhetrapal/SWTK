from setuptools import setup, find_packages
import os
import sys
setup(
    name='SWTK',
    version='1.4.6',
    description='Sort txt file from weirdest line to last. Meant to be used for Logs.An experimental Unsupervised Learning Log Anomaly Detection toolkit. YOU ARE BEAUTIFUL! This will sort the input based on weirdness',
    url='https://github.com/nileshkhetrapal/SWTK',
    author='Nilesh Khetrapal',
    packages=find_packages(),
    scripts=['bin/SWTK'],
)

if sys.platform == 'win32':
    TriePath = 'C:\\Users\\' + username + '\\AppData\\Local\\Temp\\Trie.exe'
    # Check if anomaly_detection.exe is in the temp directory
    # If anomaly_detection.exe is not in the temp directory, download it from the repository,compile it and place it in the temp directory
    if not os.path.isfile("C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Trie.exe"):
        print("Trie.exe is not in the temp directory. Downloading it from the repository...")
        os.system("curl -L https://github.com/Redempt/anomaly_analysis/releases/download/Dev_Only/anomaly_detection.exe -o Trie.exe")
        print("Trie.exe was downloaded successfully.")
        print("Moving Trie.exe to the temp directory...")
        os.system("move Trie.exe C:\\Users\\" + username +  "\\AppData\\Local\\Temp\\Trie.exe")
        print("Done.")
# If the host is linux or mac, check if the rust program is accessible

else:
    # TriePath has the location of the rust program
    #TriePath should point to the rust program in the usr/bin directory
    TriePath = '/usr/bin/trie'
    # Check if the rust program is accessible
    if not os.path.isfile(TriePath):
        #move the trie program to the usr/bin directory
        os.system("sudo mv trie /usr/bin/trie")
        print("Trie is not present. Downloading and Compiling it from the repository... This only needs to be done once.")
        if not os.path.isfile(TriePath):
            # Download the rust program from the repository to the tmp directory and compile it
            os.system("sudo wget https://github.com/Redempt/anomaly_analysis/releases/download/Linux/trie -O /usr/bin/trie")
            # Make the rust program executable
            os.system("sudo chmod +x /usr/bin/trie")
            print("Done.")
