
def sumDigits(n):
    return sum([int(i) for i in list(str(n))])


def check_digit(s):
    l = [int(s[i]) if i % 2 == 0 else 2 * int(s[i]) for i in range(len(s))]
    sum = 0
    for num in l:
        sum += sumDigits(num)
    return str(10 - (sum % 10))

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     assert (check_digit("03824999") == "1")
#     assert (check_digit("30796170") == "6")
#     assert (check_digit("31332681") == "1")
#     assert (check_digit("31332681") != "2")
#     assert (check_digit("31629648") == "2")
#     assert (check_digit("31629648") != "6")
