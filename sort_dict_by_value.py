def sort_dict(d):
	sort_me = sorted(zip(d.values(), d.keys()))
	form_new_dict = {} # create
	for data in sort_me:
		form_new_dict[data[1]] = data[0]
	return form_new_dict # return 
input_dict = {"shiva": 24, "dinesh": 22, "subash": 21, "sanath": 29}
print(sort_dict(input_dict))


def sort_dict_two(d):
	t = []
	for key, value in d.items():
		create_tmp_tuple = (value, key)
		t.append(create_tmp_tuple)
	return sorted(t)
print(sort_dict_two(input_dict))

def dwash_func(dic1):
	sorted_values = sorted(dic1.values())
	# print(sorted_values)
	sorted_dict = {}
	for x in sorted_values:
		for k in dic1.keys():
			if dic1[k] == x:
				sorted_dict[k] = dic1[k]
				break
	print(sorted_dict)
dwash_func({'johann':52, 'k':22, "david": 12})
