import os
if not os.path.exists("c:\\temp"):
    os.makedirs("c:\\temp")

outFile = open('c:\\temp\\hellow.txt', 'w')
outFile.write('This is fun.')
outFile.close()

