import pymupdf
import json

if DE

doc = pymupdf.open("Test.pdf")

#for page in doc:
#    text = page.get_text().encode("utf8")
#    print(text)

page = doc[0]
data = page.get_text("dict",sort=False)

jdata = json.dumps(data,indent=2,default=str)

file = open("json_of_pdf.json","w")

file.write(jdata)


def find(_type="text",needle,haystack):
    for i in haystack:
        log(0,haystack)
