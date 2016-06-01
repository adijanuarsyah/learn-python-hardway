from sys import argv #sys adalah package, perintah disamping yaitu untuk mendapatkan fitur argv dari package sys.

script, filename = argv #gunakan argv untuk mendapatkan nama file.

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ") #gunakan raw input untuk ngambil nama file

txt_again = open(file_again)

print txt_again.read()
txt_again.close()
