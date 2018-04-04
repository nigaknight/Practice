list=['apple','banana','carrot','mango']
print("I have",len(list),"items to purchase.")
print("The items I want to buy are:",end=' ')
for item in list:
    print(item,end=' ')
print("\nI also want to buy the rice.")
list.append("rice")
print("Now the list is",list)
print("I will sort my list now")
list.sort()
print("The sorted list is",list)
print("The first item I want to buy is",list[0])
olditem=list[0]
del list[0]
print("Now the list is",list)