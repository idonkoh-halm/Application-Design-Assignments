#Format Strings
import re
class Name:
    first="Cody"
    middle="Jerome"
    last="West"

print '%s %s %s' % (Name.first,Name.middle,Name.last)

m=re.match("([A-Z][A-z]+) ([A-Z][A-z]+) ([A-Z][a-z]+)","Cody Jerome West")

Name.first, Name.middle, Name.last = m.groups()
print m.groups()