import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    numbers = [[10, 20, 30],
               [40, 50, 60],
               [70, 80, 90],
               [100, 110, 120]]

    ret = main.getColumn(numbers)
    print(f'Your return value is: {ret}')
    assert isinstance(ret, list)
    assert isinstance(ret[0], list), 'The element of the list should be list'
    assert ret[0] == [10, 40, 70, 100]
    assert ret[1] == [20, 50, 80, 110]
    assert ret[2] == [30, 60, 90, 120]

    # regex_string = r'[\w,\W]*1'
    # regex_string += r'[\w,\W]*3'
    # regex_string += r'[\w,\W]*5'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, main.evenlist)
    # assert res != None
    # print(res.group())
