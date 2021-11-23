python code algorithm 
START
Define a function parking with a one argument carList
Declare a variable totalSpace
Get the length of carList using len(carList)
Store output of step 4 to totalSpace
Declare an occupied
Get the count of 1 from carList using carList.count(1)
Store output of step 7 to occupied
Calculate the percentage by dividing the occupied by totalSpace and mutliplying it with 100
Return the round off value of the precentage
Declare the list which has the status of car parking spaces
Print the percentage result by invoking parking method into string.
STOP
 
 
Python Code 
#def calculate the percentage of car park space occupied
def parking(carList):
   #totalSpace is equal to length of the given list
   totalSpace = len(carList)
   #no. of slots occupied is equal to no. of 1's in the list
   occupied = carList.count(1)
   #calculating the percentage
   percentage = (occupied/totalSpace)*100
   #returning the nearest whole number for the obtained percentage
   return round(percentage)
#status list of car parking spaces
l = [1,1,0,1,0,1,1,1,1]
#printing the percentage
print("Percentage occupied is:",str(parking(l))+"%")

