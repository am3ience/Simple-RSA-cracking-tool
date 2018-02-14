import math
import gmpy #dnf install gmpy 
import time 


e = input("Enter e: ") 
n = input("Enter n :")
#e = 7
#n = 33
start_time = time.time() # timer start 
print "n = ", n

c = int(round(math.sqrt(n))) # Finding the Square Root of n

# check if it's even, if it is, go down to next odd number 
if c%2 == 0:
	c = c-1

p = 0 
# brute forcing to get prime number less than n 
def brute(c):
	p = 0 
	for i in range(c, c-40, -2):
		if (n%i) == 0:
			print "p = ", i	
			return i 

p = brute(c)

# calculate q 
q = n / p 
print "q = ", q

# calculate totient 
phin = (p-1)*(q-1)
print "totient = ", phin

# compute d using gmpy 
d = gmpy.invert(e, phin)
print "d = ", d 
#print d*e %phin #< --- if this equals 1, we're good 

#timer end 
print "This took ", ("%.5f" % (time.time() - start_time)), " seconds."