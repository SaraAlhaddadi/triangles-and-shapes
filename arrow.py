# Prepared by : Shvm-k
'''
program to print like this

   1 
  1 2 
 1 2 3 
   1 
   1 

    '''
for i in range(1,4):
 for j in range(1,5-i):
  print(" ",end='')
 for j in range(1,i+1):
  print(j,end=" ")
 print("")
for u in range(1,3):
 for j in range(1,i+1):
  print(" ",end="")
 for j in range(1,5-i):
  print(j,end=" ")
 print("")