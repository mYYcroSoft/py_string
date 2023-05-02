wight = [20,8,15,10]

stojan = []

dolls  = 4
max_weight = 20


last_num = 0


for x in enumerate(wight):
    if x[1] > 20:
      stojan.append(x)
    

max_index = 0
for x in wight: 
    max_index += 1 
print('MAXIMUM: ', max_index)


list_2 = len(wight)
for x in range(0,list_2):
    
    if wight[x] == 20:
        stojan.append(wight[x])
        print(stojan)
    else:
        if not last_num == wight[x] and wight[x] != max_index:
            print(wight[x], ' ', wight[x+1])
            if wight[x] + wight[x+1] < 20:
                stojan.append(wight[x] + wight[x+1])
                last_num = wight[x+1]
print(stojan)

          
    

    
