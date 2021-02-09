"""
Из списка A удалить те цепочки четных элементов, в которых есть хотя бы один элемент из списка B.
Пример: список A[9]: 3 2 4 5 2 3 2 6 5
список B[6]: 1 3 4 7 8 9
список A после удаления примет вид:
A[7]: 3 5 2 3 2 6 5.
"""


def get_list(length):
    i = 0
    array = []
    print('Введите числа для списка')
    while i < length:
        array.append(int(input()))
        i = i + 1
    return array


print('Введите длину первого списка')
length1 = int(input())
arrayA = get_list(length1)
print('Введите длину второго списка')
length2 = int(input())
arrayB = get_list(length2)
# arrayB = [1, 2, 3, 4]

arEvenNumbChain = {}
evenNumbsChain = []
even = 0
for index, elemA in enumerate(arrayA):
    if elemA % 2 == 0:
        if len(evenNumbsChain) == 0:
            evenNumbsChain.append(index)
            arEvenNumbChain[index] = elemA
        elif index - evenNumbsChain[-1] == 1:
            evenNumbsChain.append(index)
            arEvenNumbChain[index] = elemA
        even = index
    elif index - even == 1:
        for elemB in arrayB:
            if elemB % 2 == 0:
                if elemB in arEvenNumbChain.values() and len(evenNumbsChain) > 1:
                    continue
                else:
                    evenNumbsChain.clear()
                    arEvenNumbChain.clear()
            elif elemB not in arEvenNumbChain.values():
                evenNumbsChain.clear()
                arEvenNumbChain.clear()


res = arrayA
if len(arEvenNumbChain) >= 2:
    res = []
    for index, elem in enumerate(arrayA):
        if index in arEvenNumbChain.keys():
            continue
        else:
            res.append(elem)
print(res)














