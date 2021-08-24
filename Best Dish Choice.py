occ_list=[]
new_list=[]
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int, input().split()))
    B=A
    for j in range(1,N):
        if A[j]==A[j-1]:
            new_list.append(A[j-1])
            #B.remove(A[j-1])
        list_difference = [item for item in B if item not in new_list]
    for k in new_list:
        list_difference.append(k)
    for l in list_difference:
        occ_list.append(list_difference.count(l))
    for m in list_difference:
        if list_difference.count(m)==max(occ_list):
            best_choice=m
    print(best_choice)
