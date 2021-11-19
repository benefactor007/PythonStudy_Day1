# coding=utf-8
import bs4
from bs4 import BeautifulSoup
import lxml
import requests

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# soup = BeautifulSoup(html,'lxml')

soup1 = BeautifulSoup(open('index.html'), features="lxml")

# print soup.prettify()
print soup1.prettify()

print "soup1.title:", soup1.title
print "soup1.head:", soup1.head
print "soup1.a:", soup1.a
print "soup1.p:", soup1.p
print "soup1.p['class']:", soup1.p["class"]
print "type(soup1.a:)", type(soup1.a)

print "soup1.name:", soup1.name
print "soup1.a.name:", soup1.a.name
print "soup1.attrs:", soup1.attrs
print "soup1.p.attrs:", soup1.p.attrs  # 在这里，我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典。
print "soup1.a.attrs:", soup1.a.attrs
print "soup1.p['class']:", soup1.p['class']  # 单独获取某个属性
print "soup1.p.get('class'):", soup1.p.get('class')  ##单独获取某个属性 跟上面一样的

print "\nsoup1.a", soup1.a
print "soup1.a.string:", soup1.a.string
print "type(soup1.a.string):",type(soup1.a.string)

if type(soup1.a.string) == bs4.element.Comment:
    print soup1.a.string

print "\n\nsoup1.head.contents:",soup1.head.contents
print "soup1.head.contents[0]:", soup1.head.contents[0]
print "soup1.head.children:", soup1.head.children

# for item in soup1.body.children:
#     print item


print "\n==================================\n"


# for item in soup1.descendants:
#     print item

print "soup1.head.string:", soup1.head.string
print "soup1.title.string:", soup1.title.string
# print soup1.title.children
# for item in soup1.title.children:
#     print item
print soup1.html.string

#多个内容
for string in soup1.strings:
    print repr(string)

for string in soup1.stripped_strings:
    print repr(string)

p = soup1.p
print p.parent.name

content = soup1.head.title.string
print content.parent.name


print "\n===============================================================\n"
for parent in content.parents:
    print parent.name
print "\n===============================================================\n"


print soup1.p.next_sibling
print "\n===============================================================\n"

print soup1.p.prev_sibling
print "\n===============================================================\n"

print soup1.p.next_sibling.next_sibling

print "\n===============================================================\n"

for sibling in soup1.a.next_siblings:
    print repr(sibling)


print "\n===============================================================\n"

print soup1.head
print soup1.head.next_element
print soup1.head.next_element.next_element
print "\n===============================================================\n"

for element in soup1.head.next_elements:
    # print repr(element)
    print element

#4.  搜索文档树
print "\n############################################################################\n"

print soup1.find_all('a')
print type(soup1.find_all('a'))

print "\n############################################################################\n"
import re
for tag in soup1.find_all(re.compile("^b")):
    print tag.name
print "\n############################################################################\n"

print soup1.find_all(["a","b"])

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
print "\n############################################################################\n"

print soup1.find_all(has_class_but_no_id)

print "\n############################################################################\n"
print soup1.find_all(id="link2")

print soup1.find_all(href=re.compile("elsie"))
print soup1.find_all(href=re.compile("elsie"),id ="link1")

print soup1.find_all("a",class_="sister")

print "\n############################################################################\n"

print soup1.find_all(text="Elsie")
print soup1.find_all(text=["Tillie","Elsie","Lacie"])
print soup1.find_all(text=re.compile("Dormouse"))

print soup1.find_all("a",limit=2)

print "\n############################################################################\n"
print soup1.html.find_all("title")
print soup1.html.find_all("head",recursive=False)