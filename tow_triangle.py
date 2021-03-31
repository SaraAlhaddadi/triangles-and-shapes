# Prepared by : Shvm-k
'''
program to print like this

#####
####
###
##
#
##
###
####
#####

    '''
#the above triangular
for i in range(1,6):
 for j in range(1,7-i):
  print("#",end="")
 print("")
 
#the below triangular
for i in range(1,5):
 for j in range(0,i+1):
  print("#",end="")
 print("")