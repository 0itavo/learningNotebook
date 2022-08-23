rows = int(input("How many rows?:" ))
colomns = int(input("How many columns?:" ))
symbol = str(input("Enter the symbol:" ))

for i in range(rows):
    for j in range(colomns):
        print(symbol,end="") #end="" prevents to jump the line
    #print()
