import csv


with open("data.csv","r",encoding='utf8') as f:
    data = f.readlines()
rule = ['been update','Update new rule','fixed','structure changed','edit rule','change rule','Create new Agent for Crawl Failed Agent']
white_html = ["Site empty","white html",'blank html']
captcha = ['captcha']
status_code = ['page not found','404','403','link has died','page not working','link error','This link has been removed',"This site doesn't work anymore",'Server not found']
no_content=['html received do not have content','not have content','no content',"doesn't have content"]
no_schedule=['no schedule',"Schedule isn't set",'no scheduel',"Agent isn't set schedule"]
no_updated = ['no new updated content','no content update','no new content update','no contents update','has no new article']
permisssion = ['accounts do not have enough rights to see contents','not have enough rights to see contents',"User doesn't have permission",'does not have permission to see content','do no have enough  permission to see content','do no have enough  permission to see content']
worker = ['[]']
save_data=[]
login = ['login']
normal = ['working normally','running normal',"Agent doesn't need to be updated"]
redirect_link = ['redirect','url has been changed','url changed']
def check_issue(data,issue,issuse_name):
    count = 0
    for line in data:
        row = line.split(",",1)
        if any(text.lower() in row[1].lower() for text in issue) :
            # print(row[0])
            row[1] = issuse_name
            save_data.append([row[0],row[1]])
            count+=1
    print(issuse_name)
    print(count)


check_issue(data,rule,"rule")   
check_issue(data,white_html,"white_html")
check_issue(data,captcha,"captcha")
check_issue(data,status_code,"status_code")
check_issue(data,no_content,"no_content")
check_issue(data,no_schedule,"no_schedule")
check_issue(data,no_updated,"no_updated")
check_issue(data,permisssion,"permission")
check_issue(data,worker,"worker")
check_issue(data,login,"login")
check_issue(data,normal,"normal")
check_issue(data,redirect_link,"redirect_link")

with open("data_20_05.csv","w",encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(save_data)