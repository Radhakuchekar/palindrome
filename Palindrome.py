str1= input()
i = 0;
j = len(str1)-1
cnt= 0
lstr= list(str1)
while(i<j): 
    if lstr[i] == lstr[j]:
        i +=1
        j -=1
    else:
        if lstr[i+1] == lstr[j]:
            lstr.insert(j+1, lstr[i])            
            i +=1
        elif str1[i] == lstr[j-1]:
            lstr.insert(i, lstr[j])
            i +=1
        else:
            lstr.insert(i, lstr[j])
            i += 1
        cnt+=1
    
print(''.join(lstr))
print('count', cnt)
