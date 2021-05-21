def return_true_or_false(l):
	d = {}
	for data in l:
		if data.endswith('.rst'):
			print('data in if condition', data)
			d[data] = True
		else:
			print("data in else condition", data)
			d[data] = False
	return d
print(return_true_or_false(['one.json', 'two.txt', 'three.rst', 'four.rst', 'five.js']))
		
