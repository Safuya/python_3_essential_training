def main():
    n = 42
    s = "This is a {} string!".format(n)
    s2 = '''\
this is a string spanning many different lines of wonderful
text.
'''
    print(s)
    print(s2)

if __name__ == "__main__":
    main()
