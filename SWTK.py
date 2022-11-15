# -*- coding: utf-8 -*-
import argparse
import os
import sys
import time

#Get username
username = os.getlogin()
#Check if anomaly_detection.exe is in the current directory
if os.path.isfile("anomaly_detection.exe"):
    mutex = True
    print("anomaly_detection.exe exists.")
else:
    mutex = False
    print("anomaly_detection.exe does not exist.")
    #Compile anomaly_detection.exe from Trie_Model\src\main.rs using cargo
    print("Compiling anomaly_detection.exe...")
    #Get the current working directory
    cwd = os.getcwd()
    #Change the current working directory to Trie_Model\src
    os.chdir("Trie_Model\\src")
    #Compile anomaly_detection.exe
    os.system("cargo build --release")
    #Change the current working directory back to the original working directory
    os.chdir(cwd)
    #Copy anomaly_detection.exe from Trie_Model\src\target\release to the current directory
    os.system("copy Trie_Model\\src\\target\\release\\anomaly_detection.exe .")
    #Check if anomaly_detection.exe is in the current directory
    if os.path.isfile("anomaly_detection.exe"):
        mutex = True
        print("anomaly_detection.exe exists.")
    else:
        mutex = False
        print("anomaly_detection.exe did not compile properly.")
        sys.exit()

#Create a variable to store all the flags that have to be passed to the anomaly_detection.exe
flags = ""
#Add -a flag to the flags variable
flags += " -a"
#Get the arguments from the user
#If the user does not use a flag, assume the input file is the argument
parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file to be sorted by anomaly score.")
parser.add_argument("-o", help="Output file")
#Let the user pass a flag -m to both save/load the model
parser.add_argument("-m", help="Save/load the model")
#If the user passes the -m flag, check if the model exists

if args.m:
    #Declare a variable modelName with the value of the argument passed to the -m flag and .json appended to the end
    modelName = args.m + ".json"
    #Check if the model exists
    if os.path.isfile(modelName):
        print("Model exists.")
        #append the -m flag and the model name to the flags variable
        flags += " -l " + modelName
    else:
        print("Model does not exist, creating a new model.")
        #append the -m flag and the model name to the flags variable
        flags += " -s " + modelName
#If the user passes the -i flag, use args.i as the input file else use the argument as the input file
if args.i:
    args.input = args.i
else:
    args.input = sys.argv[1]



#Create a function to run anomaly_detection.exe with the -a flag and the input file piped in.
def run_anomaly_detection():
    #Read the input file on a line by line basis and store in a list
    with open(args.input, 'r') as f:
        lines = f.readlines()
    #Create a dictionary to store the lines and their anomaly score
    anomaly_dict = {}
    #Put the lines in the dictionary
    for line in lines:
        anomaly_dict[line] = 0
    #Run anomaly_detection.exe with the -a flag and the input file piped in.
    #The Parse the output and identify the anomaly score of the lines and sort them by the anomaly score
    #Run anomaly_detection.exe with the input file piped in and the flags variable after the input file
    with os.popen("anomaly_detection.exe " + args.input + flags) as f:
        #Read the output line by line
        for line in f:
            #Split the line by the space character
            line = line.split(" ")
            #Get the anomaly score of the line
            anomaly_score = line[0]
            #Get the line
            line = line[1]
            #Put the anomaly score in the dictionary
            anomaly_dict[line] = anomaly_score
    #Sort the dictionary by the anomaly score
    anomaly_dict = sorted(anomaly_dict.items(), key=lambda x: x[1], reverse=True)
    #If the user passes the -o flag, save the file to the output file
    if args.o:
        #Open the output file
        with open(args.o, 'w') as f:
            #Write the lines to the output file
            for line in anomaly_dict:
                f.write(line[0])
    #If the user does not pass the -o flag, print the lines to the console
    else:
        #Print the lines to the console
        for line in anomaly_dict:
            print(line[0])


def main():
    global args
    args = parser.parse_args()
    #Check if the input file exists
    if os.path.isfile(args.input):
        print("Input file exists.")
        #Check if the input file is empty
        if os.stat(args.input).st_size == 0:
            print("Input file is empty.")
            sys.exit()
        else:
            print("Input file is not empty.")
            run_anomaly_detection()
    else:
        print("Input file does not exist.")
        sys.exit()

main()