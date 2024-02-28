numbers = [int(elements) for elements in input('Enter numbers using space ').split()]
for elements in numbers:
    if elements>1:
        for devider in range(2, elements-1):
            if (elements % devider) == 0:
                print(elements, 'является составным числом')
                break
            else:
                print(elements, 'явлется простым')
                break
    else:
        print(elements, 'является не простым и не составным')