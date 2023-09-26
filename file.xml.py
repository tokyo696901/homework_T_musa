import re
urls=re.findall(r'http(?:s)?://\S+', open('file.xml').read())
print(urls)
