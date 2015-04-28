#Cody Jameson
#Project 3

#Problem 0 Part 1
def max_trans1(a,b,c):
    return min(a,b,c)

#problem 0 Part 2
def max_trans2(a,b,c,d,e):
    first = max_trans1(a,b,c)
    second = min(d,e)
    return max(first, second)

#Problem (1) Better Tip Calculator
def tip_calc(billTotal):
    tip = billTotal * (.18)
    rounded = round(tip,2)
    print("$" + str(rounded))

#Problem (2) Fancy Name Display
def nice_name():
    person = input('Enter your name: ')
    print('*********',"\n","*",person.upper(),"*",'\n','*********')

#Problem (3) Monograms-R-Us
def monogram():
    first = input('Please enter your first name: ')
    second = input('Please enter your middle initial: ')
    Third = input('Please enter your last name: ')
    print((first[0].upper(),second[0].upper(),Third[0].upper())

#Problem (4) Counting Characters
def char_ct(s1,s2,ch):
    first = str(s1,s2)
    return first.count(ch)
 
   

     

    

    
