def main():

    dictionary1 = {10: "Kurt", 20: "Jim", 30: "Bill"}
    print(dictionary1)

    IDlist, Namelist = zip(*dictionary1.items())
    print(IDlist)  # tuple
    print(Namelist)  # tuple

    for v in zip(*Namelist):
        print(v)

    #########################################


if __name__ == '__main__':
    main()
