with open("data_20_05.csv","r",encoding="utf8") as f:
    data = f.readlines()
for line in data:
    print(line)