from setuptools import setup, find_packages
import os
import sys
setup(
    name='SWTK',
    version='1.4.7',
    description='Sort txt file from weirdest line to last. Meant to be used for Logs.An experimental Unsupervised Learning Log Anomaly Detection toolkit. YOU ARE BEAUTIFUL! This will sort the input based on weirdness',
    url='https://github.com/nileshkhetrapal/SWTK',
    author='Nilesh Khetrapal',
    packages=find_packages(),
    scripts=['bin/SWTK'],
)

if sys.platform == 'win32':
    #Get username
    username = os.getlogin()
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
    #Get the username
    #use popen to get the username
    username = os.popen("whoami").read()
    homedir = os.getenv("HOME")
    # TriePath has the location of the rust program
    #Create a string with the path to the rust program
    Trie = str("/.local/bin/trie")
    TriePath = homedir + Trie
    #TriePath should point to the rust program in the usr/bin directory
    #TriePath = '/home/' + username + '/.local/bin/trie'
    # Check if the rust program is accessible
    if not os.path.isfile(TriePath):
        #move the trie program to the usr/bin directory
        print("Trie is not present. Downloading and Compiling it from the repository... This only needs to be done once.")
        
        #if not os.path.isfile(TriePath):
        if not os.path.isfile("/usr/bin/cargo"):
            os.system("sudo apt install cargo")
            print("Cargo was installed successfully.")
           
            if not os.path.isdir("~/.local/bin"):
                #check if we have permission to create the directory
                if not os.path.isdir("/usr/bin"):
                    print("You do not have permission to create the directory ~/.local/bin. Please create the directory and try again.")
                    exit()
                os.system("mkdir ~/.local/bin")
                print("The directory ~/.local/bin was created successfully.")
        
            # Download the rust program from the repository
        print("Trie is not in the /home/nilesh/bin/trie directory. Downloading it from the repository...")
        os.system("git clone https://github.com/Redempt/anomaly_analysis && cd anomaly_analysis && cargo build --release && mv target/release/trie /home/nilesh/.local/bin/trie")
        #Check if the rust program is accessible
        if not os.path.isfile(TriePath):
            print(TriePath)
            #If the rust program is not accessible, exit the program
            print("Trie is not accessible. Please check if the rust program is accessible.")
            exit()
            
           
        os.system("rm -rf anomaly_analysis")
            
        print("Done.")
