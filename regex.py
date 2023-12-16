import re

txt = "The rain in Spain"
#x = re.search("^The.*Spain$", txt)
#x = re.sub("\s", "9", txt, 2)
x = re.search(r"\bS\w+", txt)
print(x.group)
#x = re.search("ai", txt)
#print(x)