import csv
import requests
save = []
with open("data_22_02.csv","r",encoding="utf8") as f:
    reader=csv.reader(f)
    for r in reader:
        try:
            print(r)
            status_code = requests.get(r[0],timeout=20).status_code
            print(status_code)
            save.append([r[0],status_code])
        except:
            save.append([r[0],"000"])
with open("status_code.csv","w",encoding="utf8",newline='') as f:
    write=csv.writer(f)
    write.writerows(save)
