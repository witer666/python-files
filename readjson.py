import pandas
data=pandas.read_json("/Users/linux/Downloads/test.json")
print(data)
print(data['name'][1])
