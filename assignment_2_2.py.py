# ASSIGNMENT 2 : FINDING PRIME NUMBER UPTO N'TH AND SUM OF ALL PRIME NUMBER LOG VALUE 
# NAME         : SATHISH A
# DATE         : JAN-10-2023


# importing math module
from math import *
# input value 
n= int(input('enter number'))
#sum of logarithm
sum_log = 0
#for loop upto n'th
for i in range(2,n):
    #finding prime number
    count = 0
    
    for j in range(2,i+1):
        #check number is divisible by it self or not
        if i%j == 0:
            count = count + 1
    #if count value is one then it's prime number
    if count == 1:
        #print log of prime value
        print('value of log(',i,') is',{log(i)})
        # to find total sum of all prime of log
        sum_log = sum_log + log(i)
#printing sum of log of prime
print('sum of all log value is  ',sum_log)
#printing n'th value and sum of prime of logarithm
print('ratio num ',n,' and log',sum_log)
#printing ratio between n'th and sum of log of prime
print( f'num / sum of all log  = {n/sum_log}')

