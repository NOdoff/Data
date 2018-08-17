from requests import get
from bs4 import BeautifulSoup
import csv

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
nfl = BeautifulSoup(response.content, features = "html.parser")

# print(nfl.prettify())
# print(nfl.a)
# print(nfl.p)

body = nfl.body
main = body.find(id = 'main-content')
roster = main.find(summary = "Roster")
tbody = roster.find("tbody")
for row in tbody.find_all("tr"):
    a_name = row.find(class_ = "nfl-o-roster__player-name")
    name = a_name.find("a").text
    num = row.find_all("td")[1].text
    pos = row.find_all("td")[2].text
    h = row.find_all("td")[3].text
    w = row.find_all("td")[4].text
    age = row.find_all("td")[5].text.strip()
    exp = row.find_all("td")[6].text
    college = row.find_all("td")[7].text
    print(college)
    with open('college.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([college])
    with open('roster_table.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, num, pos, h, w, age, exp, college])