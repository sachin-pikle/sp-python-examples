import re

pattern = re.compile(r'Cat(egory|ch|erpillar|astrophe|)')
match = pattern.search('I have a Cat')
print(match.group())
print(match.group(1))