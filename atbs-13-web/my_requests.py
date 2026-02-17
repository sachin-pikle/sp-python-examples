## Source: https://pypi.org/project/requests/
## Docs: https://requests.readthedocs.io/en/latest/
## pip install requests

import requests

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r = requests.get('https://api.github.com', auth=('user', 'pass'))

print('Response Details:')
print('Status code: ', r.status_code)
print('Encoding: ', r.encoding)
print('\nResponse text: ', r.text)
print('\nResponse json: ', r.json())