mobil = 100
ruang_di_mobil = 4
pengemudi = 30
penumpang = 90
mobil_tidak_dikendarai = mobil - pengemudi
mobil_dikendarai = pengemudi
kapasitas_mobil = mobil_dikendarai * ruang_di_mobil
rata_penumpang_per_mobil = penumpang / mobil_dikendarai

print "Ada ", mobil, "yang tersedia"
print "Cuma ada ", pengemudi, "pengemudi yang tersedia"
print "Masih ada", mobil_tidak_dikendarai, "mobil kosong hari ini"
print "Kita bisa mengantar", kapasitas_mobil, "orang hari ini"
print "Kita punya", penumpang, "untuk diantar hari ini."
print "Kita harus menyediakan", rata_penumpang_per_mobil, "di setiap mobil"