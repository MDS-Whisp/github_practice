groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    answer = input("What item do you want to remove? Type 'stop' when finished: ")
    
    if answer == "stop":
        break
    
    if answer in groceries:
        groceries.remove(answer)
        
print(groceries)
