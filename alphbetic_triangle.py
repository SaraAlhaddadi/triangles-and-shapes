# Prepared by : Shvm-k
'''
program to print like this

     A
    AB
   ABC
  ABCD
 ABCDE

    '''
for i in range(65,70):
 for j in range(65,135-i):
  print(" ",end="")
 for j in range(65,i+1):
  print(chr(j),end="")
 print("")