### Telephone numbers
import re

pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj= pattern_obj.search("My number is +91-920-671-8752.")
print(match_obj.group())

pattern_obj = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
match_obj= pattern_obj.search("My number is +91 (920) 671-8752.")
print(match_obj.group())