
numList= [] #Array of numbers
newArr=[]
#user input loops 5 times for a number
print("[+] Please input numbers once completed type start to begin")
# for i in range(1, 6):
#     numList.append(int(input('Enter the 5 numbers: ')))

while True:
    i = input('Enter the 5 numbers, type start to begin: ')
    if i == "start":
        break
    numList.append(int(i))
print("[+] calculating now")

numList_len= len(numList) -1 #stop the main function on the last index

#Main function to do addition of the number and following number in the array

for j in range(0, numList_len):
    total = numList[j] + numList[j+1]
    newArr.append(total) #outputs numbers to the new array
print('Here are your list of numbers:', numList) #shows array
print('Final calculations:',newArr) # shows new array

#prints max
print('The maximum value is:', max(newArr))
