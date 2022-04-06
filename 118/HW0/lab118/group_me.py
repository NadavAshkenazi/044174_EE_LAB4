def group_me(f, l):
    # dict1 = {f(a): [b for b in l if f(a) == f(b)] for a in l}
    funDict = {a: f(a) for a in l}
    dict1 = dict()

    #change compx
    for a in l:
        fa = funDict[a]
        if fa not in dict1:
            dict1[fa] = [b for b in l if funDict[b] == fa]

    sortedKeys = sorted(list(dict1.keys()))
    res = {i: dict1[i] for i in sortedKeys}
    return res


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     res1 = group_me(len, ["a", "", "bb", "t", "agf", "r", "e", "", "yt"])
#     print("res1")
#     print(res1)
#     wantedRes1 = {0: ["", ""],
#                   1: ['a', 't', 'r', 'e'],
#                   2: ['bb', 'yt'],
#                   3: ['agf']
#                   }
#     print("wantedRes1")
#     print(wantedRes1)
#     assert (res1 == wantedRes1)
#
#     res2 = group_me(lambda x: x % 3, range(10))
#     print(res2)
#     wantedRes2 = {0: [0, 3, 6, 9],
#                   1: [1, 4, 7],
#                   2: [2, 5, 8]
#                   }
#     assert (res2 == wantedRes2)
