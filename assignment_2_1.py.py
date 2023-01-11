# ASSIGNMENT 1 : FINDING 450'TH PRIME NUMBER
# NAME         : SATHISH A
# DATE         : JAN-10-2023

# list to append the prime numbers
prime = []
#searching 450'th prime for every 50'th prime number 
num = 0
#loop for upto 450 th prime number is found
while len(prime) < 450:
    num = num + 1
    # code should run only odd number except 2
    if  num%2 != 0 and num > 1 or num == 2  :

        count = 0
        # range from two upto num
        for j in range(2,num+1):
          
            # check odd number is divisible by itself for one time
            if num % j == 0:
                count = count+1
        #append prime no to list       
        if count == 1 : 
            prime.append(num)
#printing the 450'th prime number
print('450 th prime number  : ',prime[450-1])  
#print the list of prime nmbers
print(prime)

#printing the No. of prime number so far
count_prime = 0
num = 50
for i in range(len(prime)):
    #check upto num
    if prime[i] <= num:
        # print(prime[i])
        count_prime = count_prime + 1
    # change num value
    else:
        # printing no. of prime upto num value
        print(count_prime,' :-  prime numbers found so far')
        # increase num value
        num = num + 50
        count_prime = count_prime + 1
        
