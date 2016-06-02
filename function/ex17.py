def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

def madu_dan_susu(madu, susu):
	print "Kamu punya %d stok madu!" % (madu)
	print "Kamu punya %d stok susu!" % (susu)
	print "Wah enak sekali! :)\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variable and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "Stok kamu sekarang :"
madu_dan_susu(10, 30)

stok_madu_sekarang = raw_input("Berapa banyak Stok madu kamu saat ini?: ")
stok_susu_sekarang = raw_input("Berapa banyak Stok susu kamu saat ini?: ")
madu_dan_susu(int(stok_madu_sekarang), int(stok_susu_sekarang))