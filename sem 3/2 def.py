
def prostmn(i,num):
    if num == 1:
        return
    if num % i == 0:
        print(i)
        return prostmn(i, num//i)
         
    return prostmn(i+1, num)

num = int(input())
prostmn(2,num)
