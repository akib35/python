from sys import argv

try:
    script, filename = argv

    txt = open(filename)
    print(f"Here is your file {filename}'s content\n", txt.read())

except ValueError | FileNotFoundError:
   exit(1)
