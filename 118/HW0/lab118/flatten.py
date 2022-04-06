def flatten(l):
    if all([not isinstance(x, list) for x in l]):
        return l
    aggregatingList = []
    for x in l:
        if isinstance(x, list):
            aggregatingList.extend(flatten(x))
        else:
            aggregatingList.append(x)
    return aggregatingList


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     assert (flatten([]) == [])
#     assert (flatten([0, 1, [2, 3], 4, [5, 6]]) == [0, 1, 2, 3, 4, 5, 6])
#     assert (flatten([0, [[[1]]], [[2, 3], [4, [[5, 6]]]]]) == [0, 1, 2, 3, 4, 5, 6])
#     assert (flatten([[[0, [[[1]]], [[[2, 3]], [], [4, [[5, 6]]]]]]]) == [0, 1, 2, 3, 4, 5, 6])
