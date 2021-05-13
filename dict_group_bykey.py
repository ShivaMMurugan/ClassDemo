def common(d1, d2, new_dict=dict()):
    intersection = [x for x in d1 if x in d2]
    for each_letter in intersection:
        new_dict[each_letter] = d1.get(each_letter), d2.get(each_letter)
    return new_dict
print(common({'a': 1, 'b': 22, 'c': 32, 'd': 44}, {'d': 4, 'a': 22}))

def common_solution_two(d1, d2):
    intersection = [x for x in d1 if x in d2]
    d = {k: (d1[k], d2[k]) for k in intersection}
    return d
print(common_solution_two({'a': 1, 'b': 22, 'c': 32, 'd': 44}, {'d': 4, 'a': 22}))
