'''
Cody Jameson
Project 1
'''
#problem 0
ttl_shirts = 10	
ttl_yellow = 4	
ttl_green = 6	
ycost =	20
gcost = 25
ttl_cost = (ttl_yellow * ycost) + (ttl_green * gcost)
print(ttl_cost)
#Answer: $230
#*****************************#
#problem 1
x=5 # 5
x=x**3 # 125
x=x-2 # 123
x # 123
#*****************************#
#problem2
x=1 # 1
x*=10 # 10
x+=x # 20
x # 20
#*****************************#
#problem3
temp = 0
ftemp = (temp * 9/5) +32
ctemp = (temp - 32) * 5/9
print(temp, ftemp, ctemp)
#*****************************#
#problem4
#Number of minutes in a non leap-year.
minutesInAHour = 60
hoursInADay = 24
daysInAYear = 365
print(daysInAYear * hoursInADay * minutesInAHour)
#ANSWER: 525600
#*****************************#
#problem5
intPrice = .01
multiplyPrice = 2
daysOfMonth = 31
increaseDays = multiplyPrice ** daysOfMonth
total = increaseDays * intPrice
print(total)
#Answer:
#31 Days:21,474,836.48
#30 Days:10,737,418.24
#28 Days: 2,684,354.56
#*****************************#
#Extra credit
'''
I will stick with starting with .01 and duplicating every day for a month unless
the month had 28 days like April.
'''




