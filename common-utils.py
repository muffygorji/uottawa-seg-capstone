import sys, os, fileinput

home_path = os.path.expanduser("~")

def replaceFileBeatPath():
    if not os.path.exists(f'{home_path}/logs'):
        os.mkdir(f'{home_path}/logs')

    for line in fileinput.input("ext-config/filebeat.yml", inplace=1):
        if "!!!!" in line:
            line = line.replace("!!!!",home_path)
        sys.stdout.write(line)

if (__name__ == "__main__"):
    replaceFileBeatPath()