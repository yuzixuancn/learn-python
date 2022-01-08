# 求数组内元素的所有组合

animals = {'小猫', '小狗', '小仓鼠'}
# animals = {'小猫'}

# def combine(st, n=2):
#     if len(st) == n:
#         return [st]
#     elif len(st) > n:
#         sets = []
#         for item in st:
#             new_st = st.copy()
#             new_st.remove(item)
#             sub_lst = combine(new_st, n)
#             for i in sub_lst:
#                 if i not in sets:
#                     sets.append(i)
#         return sets

# def combine_all(st):
#     lst = []
#     for i in range(1, len(st) + 1):
#         lst += combine(st, i)
#     return lst

# print(combine_all(animals))


def combine(st):
    if len(st) == 1:
        return [st]
    else:
        sets = [st]
        for item in st:
            new_st = st.copy()
            new_st.remove(item)
            for it in combine(new_st):
                if it not in sets:
                    sets.append(it)
        return sets


combination = combine(animals)
combination.sort(key=lambda x: len(x))
print(combination)
print('一共有{}种组合'.format(len(combination)))
