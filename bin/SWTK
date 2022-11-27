#!/usr/bin/env python3
'''
The goal of this script is to identify the weird lines of the input file.
It will utilize a rust program to find the weird lines of the input file. For windows, it must be downloaded from the repository and placed in the temp directory. For linux and mac, it must be downloaded, compiled and placed in the temp directory.
The script must check at runtime if the rust program is accessible or not.
The script will then assign an anomaly score to each line and sort the lines by the anomaly score.
The user can get the top N lines by specifying the -n flag. 
The user can specify the output file by using the -o flag. Default output is printed on the screen.
The user can specify the input file by using the -i flag. Default input is the input file name.
The user can specify if they wish to save the model by using the -s flag. Default is False.
The user can specify the model name by using the -m flag if they choose to use a saved model, it must be in the same directory as the user. Default value is to create a new model.
This script is supposed to be a pip installable package.

example_text = Example:
SWTK input.txt
SWTK -i input.txt -n 10
SWTK -i input.txt -n 10 -o output.txt
SWTK -i input.txt -n 10 -o output.txt -s  #Default model name is input.model
SWTK -i input.txt -n 10 -o output.txt -m input.model #Use the saved model
#Use the saved model and update the model
SWTK -i input.txt -n 10 -o output.txt -m input.model -s input.model
#Use the saved model and create a new model
SWTK -i input.txt -n 10 -o output.txt -m input.model -s new.model
#Use the -v flag to print the anomaly values along with the output
SWTK -i input.txt -n 10 -o output.txt -m input.model -s new.model -v yes
'''


import argparse
import os
import sys
def main():
    global args

    def prepare_input(input):
        # Get username
        username = os.getlogin()
        # Get all the user arguments
        global args
        # Get the TriePath
        # Check if the rust program is accessible
        # Figure out if the host is windows, linux or mac
        if sys.platform == 'win32':
            TriePath = 'C:\\Users\\' + username + '\\AppData\\Local\\Temp\\Trie.exe'
            # Check if anomaly_detection.exe is in the temp directory
            # If anomaly_detection.exe is not in the temp directory, download it from the repository,compile it and place it in the temp directory
            if not os.path.isfile("C:\\Users\\" + username + "\\AppData\\Local\\Temp\\Trie.exe"):
                print(
                    "Trie.exe is not in the temp directory. Downloading it from the repository...")
                os.system(
                    "curl -L https://github.com/Redempt/anomaly_analysis/releases/download/Dev_Only/anomaly_detection.exe -o Trie.exe")
                print("Trie.exe was downloaded successfully.")
                print("Moving Trie.exe to the temp directory...")
                os.system("move Trie.exe C:\\Users\\" + username +
                        "\\AppData\\Local\\Temp\\Trie.exe")
                print("Done.")
        # If the host is linux or mac, check if the rust program is accessible

        else:
            # TriePath has the location of the rust program
            #TriePath should point to the rust program in the usr/bin directory
            TriePath = '/usr/bin/Trie'
            # Check if the rust program is accessible
            if not os.path.isfile(TriePath):
                print(
                    "Trie is not present. Downloading it from the repository... This only needs to be done once.")
                os.system(
                    "git clone https://github.com/Redempt/anomaly_analysis.git")
                # Print("Sauce was downloaded successfully.")
                # Compile the rust program using cargo and name it Trie and place it in the bin directory
                os.system("cd anomaly_analysis && cargo build")
                print("Trie was compiled successfully.")
                # Move the rust program to the bin directory
                os.system("sudo mv /target/debug/Trie /usr/bin/")
                print("Trie was moved to the bin directory successfully.")
                #Move out of the anomaly_analysis directory
                os.system("cd ../")
                # Remove the anomaly_analysis directory
                os.system("rm -rf anomaly_analysis")
        # Create a variable to store the the flags
        flags = "-a "
        # Check if the user wants to save the model
        if args.save:
            # Check if the user specified a model name
            # if args.model:
            # Use the model name specified by the user
            model_name = args.save
            # Append the -s flag to the flags
            flags = "-s " + model_name
            # Print("The model will be saved as " + model_name)
            print("The model will be saved as " + model_name)
            # run the Trie program with the input.txt file and the flags and store the output in a variable
            TrieOutput = os.popen(TriePath + " " + input + " " + flags).read()
            TrieOutput = os.popen(TriePath + " " + input + " " + "-a").read()
            # Check if the model was saved in the directory
            if not os.path.isfile(model_name):
                print("Model was not saved.")
                exit()
            # Check if the model is empty
            if os.stat(model_name).st_size == 0:
                print("Model is empty.")
                exit()
            # Print that the model was saved
            print("Model was saved successfully.")
        # Check if the user wants to use a saved model
        elif args.model:
            # Check if the model exists
            if not os.path.isfile(args.model):
                print("Model does not exist.")
                exit()
            # Use the model specified by the user
            model_name = args.model
            # Print the name of the model being used
            print("Using model: " + model_name)
            # Run trie with the -l flag to get the anomaly score
            TrieOutput = os.popen(TriePath + " " + input +
                                " " + "-a -l " + model_name).read()
        # Check if the user wants to use a saved model and update the model
        elif args.model and args.save:
            # Check if the model exists
            if not os.path.isfile(args.model):
                print("Model does not exist.")
                exit()
            # Use the model specified by the user
            model_name = args.model
            print("Using the saved model and updating it...")
            # Append the -l flag to the flags
            Lflag = "-l " + model_name
            # Run trie with the -l flag to get the anomaly score
            TrieOutput = os.popen(TriePath + " " + input + " -a " + Lflag).read()
            # Create flags2 to run the program again to update the model
            flags2 = "-a " "-l" + model_name + " -s " + model_name
            # Run the program again to update the model
            os.system(TriePath + " " + input + " " + flags2)
            print("Model was updated successfully.")
        # If the user has not passed any arguments, just the input file
        else:
            # Run trie with the -a flag to get the anomaly score
            # Make os.popen not print the to the screen
            TrieOutput = os.popen(TriePath + " " + input + " " + "-a").read()
            # TrieOutput = subprocess.STDOUT(TriePath + " " + input + " -a", shell=True)
            # print(TrieOutput)
        return TrieOutput
    # Check platform for username for windows
    if sys.platform == 'win32':
        # Get the username
        username = os.getlogin()
    example_text = '''Example:
SWTK input.txt
SWTK -i input.txt -n 10
SWTK -i input.txt -n 10 -o output.txt
SWTK -i input.txt -n 10 -o output.txt -s  #Default model name is input.model
SWTK -i input.txt -n 10 -o output.txt -m input.model #Use the saved model
#Use the saved model and update the model
SWTK -i input.txt -n 10 -o output.txt -m input.model -s input.model
#Use the saved model and create a new model
SWTK -i input.txt -n 10 -o output.txt -m input.model -s new.model
#Use the -v flag to print the anomaly values along with the output
SWTK -i input.txt -n 10 -o output.txt -m input.model -s new.model -v yes'''
    # Setup the argument parser
    parser = argparse.ArgumentParser(
        description="The goal of this script is to identify the weird lines of the input file. This is made with love by Nilesh Khetrapal. Protip: YOU ARE BEAUTIFUL!",
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "-i", "--input", help="Input file name, it must be a txt. It will not work if it is not provided", default=False, required=True)

    parser.add_argument(
        "-n", "--top", help="Number of lines to print. Default is 10", default=False)
    parser.add_argument(
        "-o", "--output", help="Output file name. Default is output.txt", default=None)
    parser.add_argument(
        "-s", "--save", help="Save the model. Default is False. Use this flag if you want to update a model loaded through -m", default=False)
    parser.add_argument(
        "-m", "--model", help="Model name. Default is to create a new one for this runtime and delete it after the script is done running.", default=None)
    # Add another parser argument to specify if the users wants to see the Values through -v
    parser.add_argument(
        "-v", "--values", help="Show the values of the anomalies. type yes after -v to see the values", default=False)
    args = parser.parse_args()
    # Get the raw arguments passed to the script and store them in a variable
    raw_args = sys.argv
    # If the -i flag is not passed, use raw_args as the input file
    if not args.input:
        input = raw_args[1]
    # Check if the input file exists
    # A variable InputFilePath to store the path of the input file, which is the current directory + the input file name
    # if os is windows, use \ instead of /
    if sys.platform == 'win32':
        InputFilePath = os.getcwd() + "\\" + args.input
    else:
        InputFilePath = os.getcwd() + "/" + args.input
    # print(InputFilePath)
    if not os.path.isfile(InputFilePath):
        print(args.input)
        print("Input file does not exist.")
        exit()
    # Check if the input file is empty
    if os.stat(args.input).st_size == 0:
        print("Input file is empty.")
        exit()

    # Read the input file on a line by line basis and store in a list
    with open(args.input, 'r') as f:
        lines = f.readlines()
    # Create a dictionary to store the lines and their anomaly score
    anomaly_dict = {}
    # Put the lines in the dictionary
    for line in lines:
        anomaly_dict[line] = 0
    # Get the Trie Output
    TrieOutput = prepare_input(InputFilePath)
    # pRINT THE Trie output
    # print("This is the Trie output")
    # print(TrieOutput)
    # print("This is the Trie output")
    # The TrieOutput looks like this:
    ''' 1: 6.2894735
        2: 18.783783
        3: 18.783783
        4: 18.783783
        5: 18.783783
        6: 16.893618
    '''
    # Where the first number is the line number and the second number is the anomaly score
    # X: Y
    # Get all the Y values and store them in a list
    anomaly_scores = []
    for line in TrieOutput.split('\n'):
        if line:
            anomaly_scores.append(float(line.split(':')[1]))

    # print("This is the anomaly scores")
    # print(anomaly_scores)
    # Create a new Dictionary where the key is the Line from the input file and the value is the anomaly score
    anomaly_dict = {lines[i]: anomaly_scores[i] for i in range(len(lines))}
    print("This is the anomaly dict")
    print(anomaly_dict)
    # Sort the dictionary based on the anomaly score
    sorted_anomaly_dict = dict(
        sorted(anomaly_dict.items(), key=lambda item: item[0]))
    keys = []
    values = []
    # Print all the lines and their values
    for key, value in sorted_anomaly_dict.items():
        # Add the value key to a list named values

        values.append(value)
        # Add the key to a list named keys

        keys.append(key)

    # If the -n flag is given with an integer n, store the first n lines from sorted_anomaly_dict in a new dictionary called top_n_dict
    if args.top:
        print("Printing the top " + args.top + " lines")
        # Convert the string to an integer
        top_n = int(args.top)
        # If the integer is less than 0, print an error message and exit
        if top_n < 0:
            print("The number of lines to print must be a positive integer.")
            exit()
        # If the integer is greater than the number of lines in the input file, print an error message and exit
        if top_n > len(lines):
            print(
                "The number of lines to print is greater than the number of lines in the input file.")
            exit()
        # Store the first n lines in a new dictionary
        top_n_dict = {k: v for k, v in sorted_anomaly_dict.items() if k in list(
            sorted_anomaly_dict.keys())[:top_n]}
        # Replace the sorted_anomaly_dict with the top_n_dict
        sorted_anomaly_dict = top_n_dict
        # print(sorted_anomaly_dict)
        keys = []
        values = []
    # Print all the lines and their values
    for key, value in sorted_anomaly_dict.items():
        # Add the value key to a list named values

        values.append(value)
        # Add the key to a list named keys

        keys.append(key)

    # if -v is passed
    if args.values:
        # Print the keys and Values in the Keys:Values format
        for i in range(len(keys)):
            print(keys[i] + ":" + str(values[i]))
    else:
        # Print all the lines from keys but skip empty lines
        for key in keys:
            if key:
                print(key)

    # Check if the user wants to save the output to a file and has the values flag
    if args.output and args.values:
        # Open the output file in write mode
        with open(args.output, "w") as f:
            # Write the keys and values to the file
            for i in range(len(keys)):
                f.write(keys[i] + ":" + str(values[i]) + "\n")
        print("Output file created.")
    if args.output and not args.values:
        # Open the output file and write the lines to it
        with open(args.output, 'w') as f:
            for key in keys:
                if key:
                    f.write(key)
        print("Output file created.")


main()
