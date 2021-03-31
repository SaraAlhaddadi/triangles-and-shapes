# Prepared by : Shvm-k
'''
program to print custome shape 
example:

enter tow or more characters >>> ASE
 
ASEESA
AS  ES
A    E
A    A
AS  AS
ASEASE

    '''
s=input("enter tow or more characters >>> ")
print(" ")
for i in range(1,len(s)+1):
 for j in range(0,len(s)+1-i):
  print(s[j],end="")
 for j in range(1,i):
  print(" ",end="")
 for j in range(1,i):
  print(" ",end="")
 for j in range(len(s)-1,i-2,-1):
  print(s[j],end="")
 print("")
for i in range(1,len(s)+1):
 for j in range(0,i):
  print(s[j],end="")
 for j in range(1,len(s)-i+1):
  print(" ",end="")
 for j in range(1,len(s)-i+1):
  print(" ",end="")
 for j in range(0,i):
  print(s[j],end="")
 print("")