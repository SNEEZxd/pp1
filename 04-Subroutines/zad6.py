def phoneKeypad():
    x = ''
    for i in range(1,10):
        x += f'{i} '
        if i % 3 == 0:
            print(x)
            x = ''
phoneKeypad()