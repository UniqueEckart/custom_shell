import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)


def touch(source_file):
    split = source_file.split('.')
    try:
        open(f'{split[0]}.{split[1]}', 'w')
    except OSError:
        print("Es ist ein Fehler beim erstellen der Datei passiert")
    else:
        print("Die Datei wurde erfolgreich erstellt")


def deletefile(source_file):
    try:
        os.remove(source_file)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden")
    except OSError:
        print("Es ist ein Fehler beim löschen der Datei aufgetreten")
    else:
        print("Die Datei wurde erfolgreich gelöscht")


def ren(source_file, new_file):
    try:
        os.rename(source_file, new_file)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden")
    except OSError:
        print("Es ist ein Fehler aufgetreten")
    else:
        print("Die Datei wurde erfolgreich umbenannt")
