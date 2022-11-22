import math


def f(x: float) -> float:
    """This function calculates variant 10 of lab-1.
    Takes float param x and returns result of float type.
    The domain of x is : x>9, x!=11"""
    tmp = ((math.pi*25)/(math.e*55))*(4/((x+6)*(x-11)))  # tmp to make formula shorter
    result = math.sin(2/58)-tmp-13*math.cos(x+12)+math.log((x-9), 12)
    return result


def _convert_and_check():
    """This function converts input data to float, and
    if this data cannot be converted, returns None"""
    try:
        input_data = float(input('Enter float param x (x>9 , x!=11)\n'))
    except BaseException:
        return None
    else:
        return input_data


def _check_f(x):
    """This function checks errors in f(x).
    If there is a error, returns none,
    else returns result of f(x)"""
    try:
        result = f(x)
    except BaseException:
        return None
    else:
        return result


def main():
    """Final function that uses all secondary functions and f(x) to solve the lab-1
    task and prints result. If  x is out of domain, result prints as undefined"""
    print("This function is coded by Kirill Krocha from K-10 group")
    print("This function calculates variant 10 of lab-1")
    x = _convert_and_check()
    if x is None:               # None type of x means error while converting
        print('wrong input')
    else:
        print('***** do calculations ...', end=' ')
        res = _check_f(x)
        print('done')
        print('for x =', end=' ')
        print(f'{x:.{8}f}')
        print('result =', end=' ')
        if res is None:         # None type of res means x is out of domain
            print('undefined')
        else:
            print(f'{res:.{8}f}')


main()