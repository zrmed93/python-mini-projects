import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact med@test.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
