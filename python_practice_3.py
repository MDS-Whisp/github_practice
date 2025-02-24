groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
while True:
    answer = input("what item do you want to remove? type stiop when finished: ")
    groceries.remove(answer)
    if answer == "stop":
        break

print(groceries)