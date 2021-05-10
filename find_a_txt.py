# 1
def search(word, sentence):
	if word in sentence:
		return True
	else:
		return False

print(search('ssh', 'secure shell hashing is also known as ssh'))

import re
#2
def using_regex(word, sentence):
	match = re.search(word, sentence)
	if match:
		return True
	else:
		return False

print(using_regex('ssh', 'secure shell hashing is also known as ssh'))

# 3
def using_string_find_method(word, sentence):
	match = sentence.find(word)
	if match != -1:
		return True
	else:
		return False
print(using_string_find_method("ssh", "secure shell hashing is also known as ssh"))

#4
import operator
def using_operator(word, sentence):
	if not operator.contains(word, sentence):
		return False
	else:
		return True
print(using_operator("secure shell hasing is also known as ssh", "ssh"))

#5
def using_string_index(word, sentence):
	try:
		if sentence.index(word):
			return True
		else:
			return False
	except ValueError as e:
		print(e.message, "cannot find a index for the given word => {}, hence returning None".format(word))
print(using_string_index("ssh", "secure shell hashing is also known as ssh"))
