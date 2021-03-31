# Prepared by : Shvm-k
'''
program to print like this

---------1
--------121
-------12421
------1248421
-----1248168421
----12481632168421
---124816326432168421
--12481632641286432168421

    '''
for i in range(0,8):
 for j in range(0,9-i):
  #print - triangular
  print("-",end="")

#print numbers in triangular
 for j in range(0,i+1):
  print(2**j,end="")
 for j in range(i-1,-1,-1):
  print(2**j,end="")
 
 print("")