def hitung_segi(alas, tinggi):
	print "Luas segitiga: %d" % ((alas*tinggi)/2)

#Cara ke 2
def hitung_luas(alas, tinggi):
	return ((alas*tinggi)/2)

input_alas = raw_input("Masukkan alas segitiga: ")
input_tinggi = raw_input("Masukkan tinggi segitiga: ")

hitung_segi(int(input_alas), int(input_tinggi))

#Cara 2
luas = hitung_luas(int(input_alas), int(input_tinggi))
print "Luas segitiga: %d" % (luas)