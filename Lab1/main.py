"""
Из списка A удалить те цепочки четных элементов, в которых есть хотя бы один элемент из списка B.
Пример: список A[9]: 3 2 4 5 2 3 2 6 5
список B[6]: 1 3 4 7 8 9
список A после удаления примет вид:
A[7]: 3 5 2 3 2 6 5.
"""


def get_list(length):
    """
    returns input list
    :param length:
    :return:
    """
    i = 0
    array = []
    print('Введите числа для списка')
    while i < length:
        array.append(int(input()))
        i = i + 1
    return array


def is_even(number):
    """
    check even
    :param number:
    :return:
    """
    return number % 2 == 0


def delete_even_chain(array_a, array_b):
    """
    remove even chain
    :return:
    """
    arEvenNumbChain = {}
    evenNumbsChain = []
    even = 0
    for index, elemA in enumerate(array_a):
        if is_even(elemA):
            if len(evenNumbsChain) == 0:
                evenNumbsChain.append(index)
                arEvenNumbChain[index] = elemA
            elif index - evenNumbsChain[-1] == 1:
                evenNumbsChain.append(index)
                arEvenNumbChain[index] = elemA
            even = index
        elif index - even == 1:
            for elemB in array_b:
                if is_even(elemB):
                    if elemB in arEvenNumbChain.values() and len(evenNumbsChain) > 1:
                        continue
                    else:
                        evenNumbsChain.clear()
                        arEvenNumbChain.clear()
                elif elemB not in arEvenNumbChain.values():
                    evenNumbsChain.clear()
                    arEvenNumbChain.clear()

    res = array_a
    if len(arEvenNumbChain) >= 2:
        res = []
        for index, elem in enumerate(array_a):
            if index in arEvenNumbChain.keys():
                continue
            else:
                res.append(elem)
    return res


print('Введите длину первого списка')
length1 = int(input())
arrayA = get_list(length1)
print('Введите длину второго списка')
length2 = int(input())
arrayB = get_list(length2)
# arrayB = [1, 2, 3, 4]
print(delete_even_chain(arrayA, arrayB))










