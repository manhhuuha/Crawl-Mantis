from get_isssue_info import *
hyundai = ['http://114.200.204.68:8080/','Hyundai In-Service']
kb = ['http://125.138.183.126/','']

save_data = get_issue_info('http://125.138.183.126/','KB Project')
save_file("data_kb_24_05.csv",save_data)