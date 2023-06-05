def getColumn(numbers):
    retval = list(zip(*numbers))
    retval = list(map(list, retval))
    return retval


def main():
    numbers = [[10, 20, 30],
               [40, 50, 60],
               [70, 80, 90],
               [100, 110, 120]]

    ret = getColumn(numbers)
    print(ret)


if __name__ == '__main__':
    main()
