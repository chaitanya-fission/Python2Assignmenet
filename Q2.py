values = input('Enter the values with "," as delimiter\n')
string_list = values.split(',')
try:
    int_list = [int(i) for i in string_list]
    int_set = set(int_list)
    new_list = []
    for i in int_set:
        cou = int_list.count(i)
        if cou > 1:
            new_list.append(i)
    new_list.sort(reverse=True)
    print(new_list)

except ValueError as ve:
    print('please, enter integer values only')
except Exception as e:
    print(str(e))
