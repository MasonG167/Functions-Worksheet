def char_stats(s):
    upper = 0
    lower = 0

    for c in s:
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1

    return upper, lower


if __name__ == '__main__':
    value = input("Enter a string")

    print('Thera are', char_stats(value)[0], 'uppercase and', char_stats(value)[1], 'lower')
