def replace(list,orignal,replace):
    if orignal == replace:
        return list
    for i in range(len(list)):
        if list[i]==orignal:
            if replace > orignal:
                while ( i != len(list)-1 and replace > list[i+1]):
                    list[i]=list[i+1]
                    i+=1
                list[i] = replace
            else:
                while (i != 0 and replace < list[i-1]):
                    list[i]=list[i-1]
                    i-=1
                list[i] = replace
            return list
    

print(replace([1,3,5,7,10],10,2))