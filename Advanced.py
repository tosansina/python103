A = [0,1,'two'] # Created list  // list() // mutable-ordered
B = 3,4,'Five' # created Tuple // tuple() // immutable-ordered
C = {'target1':'python','target2':'Image_Processing'} #Created Dictionary  //dict() // mutable - unordered -index multi type
D = {6,7,'seven'} # Created set  // set() // immutable - unordered - uniqe
#print (type(A),type(B),type(C),type(D))
#//////////////////////////////////////////////////////////////////////////////////////
a = 1
b = 2.5 
c = '3'
#print ("value a = %i, value b = %f, value c = %c"  % (a,b,c))
#/////////////////////////////////////////////////////////////////////////////////////////////
var = 0,1,2,3,4,5,6,0,7,8,9,0,0,7,100
List = [5 for i in var]
#print(List)
List1 = [i for i in var if i !=0]
#print(List1)
#////////////////////////////////////////////////////////////////////////////////////
# import only system from os 
from os import system, name 

# import sleep to show output for some time period 
from time import sleep 

# define our clear function 
def clear(): 

	# for windows 
	if name == 'nt': 
		_ = system('cls') 

	# for mac and linux(here, os.name is 'posix') 
	else: 
		_ = system('clear') 
clear() 
# print out some text 
for i in range(3):
    print(3-i)
    sleep(1) 
    clear() 
#////////////////////////////////////////////////////////////////////

List = [2,1,0]
for i,j in enumerate(List):
	print(i,j)

#//////////////////////////////////////////////////////////////////////	

