import re

pattern_obj = re.compile(r'(\d{3})-(\d{3}-\d{4})')
matches = pattern_obj.search('My phone number is +1-817-963-8162')

print("matches.group(0)", matches.group(0))
print("matches.group(1)", matches.group(1))
print("matches.group(2)", matches.group(2))
print("matches.group()", matches.group())

print("matches.groups()", matches.groups())

area_code, phone_num = matches.groups()

print("area code", area_code)
print("phone number", phone_num)