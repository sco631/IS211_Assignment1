def listDivide(numbers, divide=2): """function with 2 parameters"""

    divisble = 0                   """function returns list that are divisible by divide """
    for Num in numbers:
        if Num % divide == 0:
            divisible += 1

    return divisible


class ListDivideException(Exception):      """custom exception class"""
    pass


def testListDivide():               """ testListDivide function and raising ListDivideException """
    try:
        if not listDivide([1, 2, 3, 4, 5]) ==2:
            raise ListDivideException
        if not listDivide([2,4,6,8,10]) ==5:
            raise ListDivideException
        if not listDivide([30, 54, 63, 98, 100], divide = 10) ==2:
            raise listDivideException
        if not listDivide([1]) ==0:
             raise ListDivideException
        if not listDivide([1, 2, 3, 4,5], 1) ==5:
                raise ListDivideException
        print("All test cases passed")
    except ListDivideException:
        print("Division exception occured")

    testListDivide()                  """Calling testListDivide"""