def main():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third',
        four = 'fourth',
        five = 'fifth'
    )
    v = 'four'
    print(choices.get(v, 'other'))
0
if __name__ == "__main__":
    main()
