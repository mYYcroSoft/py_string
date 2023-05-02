dolls  = int(input("Počet loutek: "))
wight = []

for x in range(dolls):
    vaha = int(input(f"Váha loutky {x} : "))
    wight.append(vaha)

max_weight = int(input("Maxmální váha: "))

stojan = []
for x in range(len(wight)):
    if wight[x] == 0:
        continue
    for y in range(x+1, len(wight)):
        if wight[x] + wight[y] <= max_weight and wight[y] != 0:
            stojan.append(wight[x]+wight[y])
            wight[x], wight[y] = 0, 0
            break
    else:
        if wight[x] != 0:
            stojan.append(wight[x])
            wight[x] = 0

print(f"Loutky lze rozdělit na {len(stojan)} stojanů.")
print("Můj počet mozkových buňek po splnení tohoto jednoduchého úkolu: 0.1")

"""
for x in enumerate(wight):
    if x[1] > 20:
      stojan.append(x)
    

max_index = 0
def max_val():
    max_index = 0
    for x in wight: 
        max_index += 1 
    print('MAXIMUM: ', max_index)


list_2 = len(wight)
max_val()
for x in range(0,list_2):
    
    if wight[x] == 20:
        stojan.append(wight[x])
        wight.remove(wight[x])
        max_val()
        print(stojan)
    else:
        if not last_num == wight[x]:
            if not x+1 == max_index:
                print("plus")
                print(wight[x], '  | ', wight[x+1] , ' plus ', wight[x] + wight[x+1])
                if wight[x] + wight[x+1] < 20:
                     stojan.append(wight[x] + wight[x+1])
                     wight.remove(wight[x])
                     wight.remove(wight[x+1])
                     max_val()
            else:
                 print("MÍNUS")
                 print(wight[x], '  | ', wight[x-1] , ' plus ', wight[x] + wight[x-1])
                 if wight[x] + wight[x-1] < 20:
                     stojan.append(wight[x] + wight[x-1])
                     wight.remove(wight[x])
                     wight.remove(wight[x-1])
                     max_val()

print(stojan)

          
    """

    
