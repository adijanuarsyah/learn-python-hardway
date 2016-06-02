def print_two(*args): #tell to python to make function using def *define. 
#kemudian diikuti nama fungsi print_two, dan *args *asterisk args) dimana seperti argv hanya khusus untuk fungsi. diakhiri dengan : (colon/titik dua) dan mulai indentasi baru 
	arg1, arg2 = args
#setelah colon/titik dua semua indentasi yang memiliki 4spasi akan digabungkan ke print_two.
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % (arg1)

def print_none():
	print "I got nothin."

def _coba(arg1):
	print "Bisa gak ya? %r" % (arg1)

#setiap fungsi akan diakhir dengan dedenting (no indent)
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
_coba("Hello!")