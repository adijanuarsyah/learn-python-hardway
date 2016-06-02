from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0) #file python itu kayak tape drive tua di mainframe, atau sepeti dvd player. IA memiliki read head dan bisa "seek" . Setiap f.seek(0) artinya berpindah ke awal file. seek(0) artinya memindahkan file ke  0 byte(first byte) in the file.

def print_a_line(line_count, f):
	print line_count, f.readline(), #setiap f.readline() berarti membaca baris dari sebuah file. Fungsi readline returns \n pada setiap akir baris, gunakan , (koma) pada akhir baris untuk menghindari double \n pada setiap baris.

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print threee lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

