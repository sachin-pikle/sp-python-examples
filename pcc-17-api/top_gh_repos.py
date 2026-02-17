## Requests:
## Source: https://pypi.org/project/requests/
## Docs: https://requests.readthedocs.io/en/latest/
## pip install requests

## Plotly Express:
## Docs: https://plotly.com/python/getting-started/
## pip install "plotly[express]"


import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github+json", 
           "X-GitHub-Api-Version": "2022-11-28"}
res = requests.get(url, headers=headers)

res_dict = res.json()
repos = res_dict['items']

repo_names, stars = [], []

for repo in repos:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

# Make visualisation
fig = px.bar(x=repo_names, y=stars)
fig.show()