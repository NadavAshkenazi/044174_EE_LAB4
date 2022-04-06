

def collatz_sequence_length(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_sequence_length(n/2)
    else:
        return 1 + collatz_sequence_length(3*n + 1)


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     assert(collatz_sequence_length(13) == 10)
#     assert (collatz_sequence_length(1) == 1)
#     assert (collatz_sequence_length(2) == 2)
#     assert (collatz_sequence_length(3) == 8)
#     assert (collatz_sequence_length(123) == 47)
#     assert (collatz_sequence_length(54) == 113)


