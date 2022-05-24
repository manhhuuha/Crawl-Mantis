import csv
a = [[1,2,3],['a','b','c'],['x','y','z']]

with open("test.csv",'w',encoding='utf8',newline='') as f:
    writer  = csv.writer(f)
    for item in a:
        writer.writerow(item)