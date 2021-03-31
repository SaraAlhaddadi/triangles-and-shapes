# Prepared by : Shvm-k
'''
program to print like this

1   1
 2 2 
 4 4 
5   5

    '''
for i in range(1,6):
 if(i==3):
  continue
 for j in range(1,6):
  if(i==j or j+i==6):
   print(i,end="")
  else:
   print(" ",end="")
 print("")