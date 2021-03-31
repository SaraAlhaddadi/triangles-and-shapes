# Prepared by : Shvm-k
'''
program to print like this

   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
    '''
for i in range(1,5):
 for j in range(1,5-i):
   print(" ",end="")
 for j in range(1,i+1):
  print("*",end=" ")
 print("")
for i in range(1,4):
 for j in range(1,i+1):
  print(" ",end="")
 for h in range(1,5-i):
  print("*",end=" ")
 print("") 