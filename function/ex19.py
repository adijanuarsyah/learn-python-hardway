def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def substract(a, b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b

def multiply(a, b):
	print "DIVIDING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

def panggil(a):
	print "Apa sih? %s" %(a)
	return a

print "Let's do some math with just functions!"
print "Input number :"
a = float(raw_input("Angka pertama : "))
b = float(raw_input("Angka kedua : "))

age = add(a, b)
height = substract(a, b)
weight = multiply(a, b)
iq = divide(a, b)
nama = panggil("Adi")

print "Age: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

# A Puzzle for the extra credit, type it in anyway.
print "Here is a Puzzle."

what = add(age, substract(height,multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"