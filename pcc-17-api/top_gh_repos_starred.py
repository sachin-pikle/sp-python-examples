## Source: https://pypi.org/project/requests/
## Docs: https://requests.readthedocs.io/en/latest/
## pip install requests

import requests

url = 'https://api.github.com/search/repositories'
url += '?q=language:python+sort:stars+stars:>10000'

headers = {"Accept": "application/vnd.github+json", 
           "X-GitHub-Api-Version": "2022-11-28"}
res = requests.get(url, headers=headers)

res_dict = res.json()
print(res_dict.keys())

print(f'Total repos: {res_dict['total_count']}')
print(f'Complete results? {not res_dict['incomplete_results']}')

repos = res_dict['items']
print(f'Repos returned: {len(repos)}')

# first_repo = repos[0]
# print(f'\nKeys: {len(repos)}')
# for key in sorted(first_repo.keys()):
#     print(key)
# print('\nSelected information about the first repo: ')
# print(f'Name: {first_repo['name']}')
# print(f'Owner: {first_repo['owner']['login']}')
# print(f'Stars: {first_repo['stargazers_count']}')
# print(f'Repository: {first_repo['html_url']}')
# print(f'Created: {first_repo['created_at']}')
# print(f'Updated: {first_repo['updated_at']}')
# print(f'Description: {first_repo['description']}')

for repo in repos:
    print(f'Name: {repo['name']}')
    print(f'Owner: {repo['owner']['login']}')
    print(f'Stars: {repo['stargazers_count']}')
    print(f'Repository: {repo['html_url']}')
    print(f'Created: {repo['created_at']}')
    print(f'Updated: {repo['updated_at']}')
    print(f'Description: {repo['description']}\n')