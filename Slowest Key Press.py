def slowestKey(keyTimes):
    key_time=0
    key_times_list=[]
    key_list=[]
    key_times_dict={}
    for i in keyTimes:
        key_times_list.append(i[1]-key_time)
        key_list.append(i[0])
        key_time=i[1]
    for i in range(len(key_list)):
        key_times_dict[key_list[i]]=key_times_list[i]
    max_time_key=max(key_times_dict, key=key_times_dict.get)    
    print(key_dict[max_time_key])    
        
if __name__=='__main__':
    n= int(input())
    keyTimes=[]
    key_dict={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    for i in range(n):
        keyTimes.append(list(map(int, input().split())))
    slowestKey(keyTimes)    
