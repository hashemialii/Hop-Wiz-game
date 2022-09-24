for i in range(1, 101):
    if i % 21 == 0:
        print('Hop Wiz')
    elif i % 7 == 0:
        print('Wiz')
    elif i % 3 == 0:
        print('Hop')
    else:
        print(i)


print('===========================================')


for i in range(1, 100):
    decision = 'HopWiz' if not i % 21 else 'Hop' if not i % 3 else 'Wiz' if not i % 7 else str(i)
    print(decision)


print('===========================================')

#
for i in range(1, 101):
    decision = 'Hop-Wiz' if i in range(0, 102, 21) \
        else 'Hop' if i in range(0, 102, 3) \
        else 'Wiz' if i in range(0, 102, 7) \
        else str(i)
    print(decision)


print('===========================================')


for i in range(1, 101):
    divisible = 'HopWiz' if i % 21 == 0 else 'Wiz' if i % 7 == 0 else 'Hop' if i % 3 == 0 else str(i)
    print(divisible)

