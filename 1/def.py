

def table(n1, n2):
    for n1 in range(n1, 10):
        for n2 in range(n2, 10):
            print(f'{n1} x {n2} = {n1 * n2}')


def set_registre(s):
    if ' ' in s:
        s = s.upper()
    else:
        s = s.lower()
    return s


def get_sum(*args):
    return sum(args)


print(get_sum(1, 5, 10, 20))