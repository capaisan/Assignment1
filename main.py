class ListDivideException(Exception):
    pass


def list_divide(numbers, divide=2):
    number = 0
    for i in numbers:
        if (i % divide) == 0:
            number += 1
    print(number)
    return number


def test_list_divide():
    try:
        assert list_divide([1, 2, 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10]) == 5
        assert list_divide([30, 54, 63, 98, 100], 10) == 2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5], 1) == 5
    except Exception as e:
        raise ListDivideException(e)


test_list_divide()
