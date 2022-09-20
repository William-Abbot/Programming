import random
import time

incorrect_count = 0
counter = 0
x = True
t0 = time.time()
while x:
    print('')
    num = random.choice([1,2,3,4])
    b = True
    while b:
        try:
            i = int(input(str(num)+": "))
        except ValueError:
            continue
        if i > 4 or i < 1:
            b = False
            x = False
        if i != num:
            incorrect_count += 1
        else:
            b = False
            counter += 1

t1 = time.time()

print('\n'+str(incorrect_count))
print('\n'+str((counter/(t1-t0))+0.09*(counter+incorrect_count))+' numbers/s')