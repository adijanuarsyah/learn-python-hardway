from sys import argv #import modules digunakan untuk menjaga file agar ukurannya tetap kecil berdasarkan kebutuhan pada program yang akan dibuat. 
#modules akan memberikan fitur pada program.
#import modules maksudnya adalah import sys module, biasanya disebut libraries. atau modules saja.
#argv --> argumen variabel 

script, first, second, third, four = argv #unpacks agrument variable, jadi daripada mengambil semua argumen sekaligus, maka di assign ke dalam 4 variabel saja.

print "The Script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your four variable is:", four
