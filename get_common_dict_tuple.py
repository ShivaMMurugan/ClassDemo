def get_common(d1, d2):
	d1_keys = d1.keys()
	d2_keys = d2.keys()
	get_intersection = set(d1_keys).intersection(d2_keys)
	new_dict = {}
	for key in get_intersection:
		new_dict[key] = d1.get(key), d2.get(key)
	return new_dict

d1 = {'a': 1, 'c': 33, 'b': 21, 'd': 43}
d2 = {'b': 1, 'd': 4}
print(get_common(d1, d2))
