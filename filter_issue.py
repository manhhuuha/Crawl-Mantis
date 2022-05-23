import csv
from ntpath import join

save_data = []
with open("data_20_05.csv","r",encoding="utf8") as f:
    data = f.readlines()
for line in data:
    url = "/".join(line.split(",")[0].split("/")[0:3])
    issue = line.split(",")[1].replace("/n",'')
    print(issue)
    if "naver" not in url:
        if "daum" not in url:
            save_data.append([url,issue])
   

with open("save_data.csv","w",encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(save_data)