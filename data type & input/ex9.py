print "How old are you?"
age = raw_input('Masukkan Umur: ') #tanda petik digunakan untuk menambah komentar sebelum input  
print "How tall are you?"
#tinggi = int(raw_input()) #konvert input ke integer supaya bisa dihitung
height = raw_input()
print "How much do you weight?"
weight = raw_input()

print "So, you're %r old, and %r heavy." % (age, weight) #koma untuk membuat satu baris
#print "Kali tinggi : %r" % (tinggi * tinggi)
print "Kali tinggi : %r" % (height * height) #-- ini jadi error
#karena, tipe data raw_input secara default adalah string
# Traceback (most recent call last):
#   File "ex9.py", line 11, in <module>
#     print "Kali tinggi : %r" % (height * height)
# TypeError: can't multiply sequence by non-int of type 'str'