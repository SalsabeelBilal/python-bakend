
numebr=int(input("Enter your number "))

flag = True
if numebr<=1:
   print("not a prime number")
else:
   for i in range(2, numebr):
       if numebr%i==0:
        flag = False
        break
       
if flag:
   print("prime")
else:
   print("not prime")
