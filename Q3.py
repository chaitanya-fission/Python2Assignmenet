string = input('Enter  a string\n')
char_list = list(string)
new_list = []
try:
    for i in char_list:
        if i.isupper():
            new_list.append(i.lower())
        elif i.isspace():
            new_list.append('-')
        else:
            new_list.append(i.upper())
    print(''.join(new_list))

except ValueError as ve:
    print('please, enter integer values only')
except Exception as e:
    print(str(e))
