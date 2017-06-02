values = input('Enter the values with space as delimiter\n')
string_list = values.split()
try:
    a = int(string_list[0])
    b = int(string_list[1])
    print(a/b)
except Exception as e:
    print(e)

