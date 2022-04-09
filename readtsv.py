import pandas
data=pandas.read_table("/Users/linux/Downloads/test.tsv", sep="\\t",engine='python')
print(data)
print(data["name"][1])
