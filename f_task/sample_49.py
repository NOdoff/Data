from requests import get

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
print(response.status_code)
