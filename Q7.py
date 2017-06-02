import random


def line():
    n_list = []
    for i in range(10):
        if i < 9:
            n_list.append(str(random.randint(1,99)))
            n_list.append(',')
        else:
            n_list.append(str(random.randint(1,99)))
    return ''.join(n_list)

f = open("randomnumbers.txt",'a')
for i in range(20):
    f.write(line())
    f.write('\n')
f.close()

f_r = open("randomnumbers.txt",'r')
lines = f_r.readlines()
string_line = lines[6]
string_list = string_line.split(',')
print(string_list[4])
f_r.close()
