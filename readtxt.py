import pandas
data=pandas.read_table("/Users/linux/Downloads/test.txt", sep="\\n",engine='python')
print(data["name"][1])
