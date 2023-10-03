list = ["bla",4,"wwe", "dsdf"]

list[0]="hejejehejehjeeh"
list.append("affafafa")
list.pop(3)

print(len(list))
for list in list:
    print(list)



list1=[]
while True:   
    list1.append(input("skriv nåt roligt (sluta=q)(ta bort=x) "))
    
    if "x" in list1:
        while True:
            try:
                tabort=int(input(f"vilken vill du tabort? "))
                if 1<=tabort <= len(list1):
                    list1.pop(len(list1)-1)
                    list1.pop(tabort-1)
                    print(list1)
                    break
                else:
                    print(f"skriv rätt")
                    continue
            except:
                print(f"skriv siffra")
                continue
    elif "q" in list1:
        break
    else:
        print(list1)
        print(len(list1))

    
my_library={"name": "Volvo 740" , "utg.": 1984 , "color": "vit" }
print("min favorit bil är en" ,my_library["name"] , "med färgen" , my_library["color"] , "och utgivningen" , my_library["utg."])
