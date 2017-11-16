def read_input():
    print("Enter the string you which to reverse with spaces")
    data = input()
    return list(data.replace(' ', ''))


def rev_str(s):
    if len(s) == 1:
        return s
    else:
        rev_list = rev_str(s[1:])
        rev_list.append(s[0])

    return rev_list


def main():
    s = read_input()
    result = rev_str(s)
    print("Reversed string is ", ''.join(result))


if __name__ == '__main__':
    main()
