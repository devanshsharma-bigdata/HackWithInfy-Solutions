T=int(input())
for i in range(T):
    pile_list=list(map(int, input().split()))
    if pile_list[0]+pile_list[1]+pile_list[2]==pile_list[3]+pile_list[4]:    
        print('YES')
    else:
        print('NO')
