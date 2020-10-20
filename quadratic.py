#SAILESH PANDEY

#	Python Program to Solve Quadratic Equation
import cmath #importing maths

a = 2
b = 3
c = 4

det = (b**2) - (4*a*c)
first = (-b-cmath.sqrt(det))/(2*a)
second = (-b+cmath.sqrt(det))/(2*a)

print(' Solutions : {0} and {1}'.format(first,second))