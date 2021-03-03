import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)


def makedir(name):
    try:
        os.mkdir(name)
    except OSError:
        print("Das Verzeichniss konnte nicht erstellt werden.")
    else:
        print("Das Verzeichniss " + name + " wurde erfolgreich erstellt")


def removedir(name):
    try:
        os.rmdir(name)
    except OSError:
        print("Das Verzeichniss konnte nicht gelöscht werden")
    else:
        print("Das Verzeichniss " + name + " wurde erfolgreich gelöscht")


def listdir():
    print(os.listdir(os.getcwd()))


def move(pathx):
    if os.path.exists(pathx):
        os.chdir(pathx)
    else:
        print("This Path does not exist")
