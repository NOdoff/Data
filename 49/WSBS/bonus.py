from requests import get
from bs4 import BeautifulSoup
import csv

url = "https://www.nba.com/warriors/stats"

response = get(url)
nfl = BeautifulSoup(response.content, features = "html.parser")

body = nfl.body
# content = body.find(class_ = "content-wrap fi-basic-template")
# page = content.find(class_ = "fi-boxed-page")
# section = page.find(class_ = "section")

# browser = section.find(id = "team-players-by-browser")
# #row = browser.find('div', class_ = "row")
# tbody = browser.find('div', class_ = "fi-p--hub")


# #with open('test.csv', 'a') as csv_file:
# #        writer = csv.writer(csv_file)
# #        writer.writerow([no])

names = []
nums = []
poses = []

print('Name' + ' | ' + 'Number' + ' | ' + 'Position')
for row in body.find_all("tr"):
    a_name = row.find(class_ = "playerInfo")
    if a_name is not None and row is not None:
        num = a_name.find(class_ = "playerNumber")
        name = a_name.find("a")
        pos = a_name.find(class_ = "playerPosition")
        if num is not None and name is not None and pos is not None:
            name = name.text
            num = num.text
            pos = pos.text
            if name not in names:
                names.append(name)
            if num not in nums:
                nums.append(num)
            if len(poses) < 15:
                poses.append(pos)
for i in range(len(names)- 1):
    print(names[i] + ' - ' + nums[i] + ' - ' + poses[i])
                # print(name + ' - ' + num + ' - ' + pos)
            

    