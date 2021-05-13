import itertools
data_list = [ 
{
'country': 'USA', 
'state': 'Colorado', 
'name': 'Ariyana'
}, 
{
'country': 'USA', 
'state': 'Missouri', 
'name': 'Michelle'
}, 
{
'country': 'SA', 
'state': 'Pretoria', 
'name': 'Elon Musk'
},
{
'country': 'SA', 
'state': 'Pretoria', 
'name': 'ABD'
}, 
{
'country': 'Finland', 
'state': 'Helsinky', 
'name': 'Linux Torvalds'
},
{
	"country": "India",
	"state": "Bengaluru",
	"name": "Virat"
},
{
	"country": "India",
	"state": "Kerala",
	"name": "Mithun"
}
]


group_aggregate = itertools.groupby(data_list, key=lambda data: data['country'])
for country, actual_records in group_aggregate:
	print(country)
	for record in actual_records:
		print(record)
	print

record1 = dict(zip('helowsrfd', range(1, 10)))
record2 = dict(zip('abc', range(1, 4)))
for k, v in itertools.izip_longest(record1, record2, fillvalue="Iteration Exhausted"):
	print(k, v)
