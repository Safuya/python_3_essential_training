def main():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    for k in sorted(d.keys()):
        print(k, d[k])

    d2 = dict(
        one = 1, two = 2, three = 3, four = 4, five = 5
        )
    d2['seven'] = 7
    for k in sorted(d2.keys()):
        print(k, d2[k])

if __name__ == "__main__":
    main()
