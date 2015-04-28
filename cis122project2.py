#Cody Jameson project 2

# problem 0
def kilo_to_miles(x):
	x = x / 1.6
	return(x) 

#problem 1
def tip_calc(a):
    b = a * 0.15
    c = a * 0.18
    d = a * 0.20
    return(b,c,d)

#problem 2
#a
def convert_to_celcius(c):
    c = (c - 32) * 5/9
    return c

#b
def convert_to_fahrenheight(f):
    f = (f * 9/5) + 32
    return f

#problem 3
#a
def chirps_to_ftemp(chirps):
    ftemp = chirps + 40
    return ftemp
#b
def chirps_to_ctemp(chirps):
    ctemp = (chirps / 3) + 4
    return ctemp 

#c
def chirps_to_ctemp2(z):
    first = chirps_to_ftemp(z)
    second = convert_to_celcius(first)
    return second

#problem 4
def minimum_payment(payment):
	if(payment<15):
		return(payment)
	percentage = 0.025 * payment
	return(max (percentage, 15))
#Extra credit
#a
Binary to Decimal
100011 = 35
11 = 3 
101010 = 42
111111 = 63
Decimal to Binary
64 = 01000000
44 = 00101100
22 = 00010110
1 =  00000001

#b
4
96
1
14




        
        
            
        
        

