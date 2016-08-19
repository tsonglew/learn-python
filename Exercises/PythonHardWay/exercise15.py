from sys import argv

script,filename=argv
#Line1-3 uses argv to get a filename.
txt=open(filename)

print"Here's your file %r:"%filename#a little message
print txt.read()#Function on txt named read

print"Type the filename again:"
file_again=raw_input(">")

txt_again=open(file_again)

print txt_again.read()
