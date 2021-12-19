# 4.6 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay.
# Pay should be the normal rate for hours up to 40 and time-and-a-half
# for the hourly rate for all hours worked above 40 hours.
# Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation. The function should return a value.
# Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75). You should use input to read a string and float()
# to convert the string to a number.
# Do not worry about error checking the user input unless you want to -
# you can assume the user types numbers properly.
# Do not name your variable sum or use the sum() function.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

# Code from Autograder:
def computepay(h,r):
    if h > 40:
        reg_pay = h * r
        #print("Regular")
        overtime =  (h - 40.0) * (r * 0.5)
        #print("Overtime")
        p = reg_pay + overtime
    else:
        p = h * r
    return p

hrs = input("Enter Hours:")
hr = input("Enter rate: ")
h = float(hrs)
r = float(hr)
p = computepay(h,r)
print("Pay",p)

#p2 = computepay(h,r*2)
#print("Pay",p2)

#def computepay(h,r):
#    hrs = input("Enter Hours:")
#    h = float(hrs)
#    r = float(hr)
#    if h > 40:
#        print('Overtime')
#        reg_pay = h * r
#        overtime =  (h - 40.0) * (r * 0.5)
#        print(reg_pay, overtime)
#        xp = reg_pay + overtime
#    else:
#        print("Regular")
#        xp = h * r
#    print('Pay:',xp)
#    p = computepay(10,20)
#    return(p)
#print("Pay",p)
