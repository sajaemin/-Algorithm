N = int(input())
DS = int(input())
N_n =[]
count = 0
for i in range(N-1):
    a = int(input())
    N_n.append(a)

N_n.sort()

try:
    
    
    while N_n[-1] >= DS :
        N_n[-1] -= 1
        DS  +=1 
        count +=1
        N_n.sort()
        if N_n[-1] == DS:
            N_n[-1] -= 1
            DS  +=1 
            count +=1
        elif N_n[-1] < DS:
            break
    print(count)


except IndexError:
    count = 0
    print(count)