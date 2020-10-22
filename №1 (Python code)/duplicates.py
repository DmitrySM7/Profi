def duplicatekiller(a: list):
    """Return an array with no duplicate elements"""

    n =[]
    for i in a:
        if i not in n:
            n.append(i)
    return n


if __name__ == "__main__":
    a = input().split()
    print(duplicatekiller(a))