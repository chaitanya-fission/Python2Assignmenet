def isPrime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        count = 0
        for i in range(2,int(num/2)):
            if(num%i==0):
                count = 1
                break
        if(count == 0):
            return False
        return True

values = input('Enter the values with space as delimiter\n')
string_list = values.split()
try:
    int_list = [int(i) for i in string_list]
    for i in int_list:
        if isPrime(i):
            print('Yes')
        else:
            print('No')
except ValueError as ve:
    print('please, enter integer values only')
except Exception as e:
    print(str(e))



