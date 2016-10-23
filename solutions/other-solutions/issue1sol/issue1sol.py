def pos(num,no_list) :
    if num > 0 :
        no_list.append(num)
        return pos(num-5,no_list) 
    else :
        no_list.append(num)
        return num


def neg(num,n,no_list) :
    if num == n  :
        no_list.append(num)
        return num 
    else :
        no_list.append(num)
        neg(num+5,n,no_list)


x=raw_input()
nos = list()
i=0
while i<int(x) :
    nos.append(int(raw_input()))
    i+=1
for no in nos :
    no_list=list()
    pos(no,no_list)
    last_index = len(no_list)
    neg(no_list[-1],no,no_list)
    del no_list[last_index-1]
    print ' '.join(str(v) for v in no_list)
    