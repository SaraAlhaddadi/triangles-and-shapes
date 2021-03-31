# Prepared by : Shvm-k
#program to print like this
'''
12345    
 1234   
  123  
   12 
    1
    '''
for i in range(5,0,-1):
 for j in range(5,0,-1):
  if(i==j):
   for s in range(1,6):
    if (s<=i):
     print(s,end="")
  else:
    print(" ",end="")
 print("")