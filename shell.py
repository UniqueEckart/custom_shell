import os
from Shell.Commands.directory import makedir
from Shell.Commands.directory import listdir
from Shell.Commands.directory import move
from Shell.Commands.directory import removedir
from Shell.Commands.filemanagment import touch
from Shell.Commands.filemanagment import deletefile

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)

dictionary = {
    'mkdir': makedir,
    'ls': listdir,
    'cd': move,
    'rmdir': removedir,
    'touch': touch,
    'rm': deletefile,
            }

while True:
    user_input = input("Shell > ")
    split_input = user_input.split(' ')
    if split_input[0] in dictionary:
        if split_input[0] == "mkdir":
            dictionary[split_input[0]](split_input[1])
        if split_input[0] == "ls":
            dictionary[split_input[0]]()
        if split_input[0] == "cd":
            dictionary[split_input[0]](split_input[1])
        if split_input[0] == "rmdir":
            dictionary[split_input[0]](split_input[1])
        if split_input[0] == "touch":
            dictionary[split_input[0]](split_input[1])
        if split_input[0] == "rm":
            dictionary[split_input[0]](split_input[1])
    else:
        print("There is no command such as " + split_input[0])
