import locale
fileName = "PoemUTF8.txt"
print(locale.getpreferredencoding())
fin = open(fileName,encoding="utf-8")
line = fin.readline()
while line:
    print(line,end="")
    line = fin.readline()
