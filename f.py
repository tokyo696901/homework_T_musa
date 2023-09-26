file = open("file.xml", "r", encoding = "utf-8")
strings = file.read().split("\n")
count = 0
number = 1
start = 0
for i in strings:
    while i.find("https", start, len(i)) != -1:
        start = i.find("https", start, len(i))
        if i.find("link", start, len(i)) != -1 or i.find("isPermaLink", start, len(i)) != -1 or i.find("url", start, len(i)) != -1 or i.find("</guid>", start, len(i)) != -1:
            print(i[start:i.rfind("<", start, len(i))], f"number: {number}")
        else:
            if i.find("\\", start, len(i)) == -1:
                end = i.find('"', start, len(i))
                print(i[start:end], f"number: {number}")
            else:
                end = i.find('\\', start, len(i))
                print(i[start:end], f"number: {number}")
        start +=1
        
        count += 1
        
    start = 0
    number += 1
    
print(f"Total:{count}")
    
