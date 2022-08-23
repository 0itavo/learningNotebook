#lists = used to store multiple items in a single variable

food = ["pizza","hamburgues","hotdog","café"]
print(food)
print(food[1])
food[1] = "sushi"
print(food[1])
food.append("ice cream")
food.remove("sushi")
food.pop() #remove the last one
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
    print(x)
