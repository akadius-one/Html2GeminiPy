import os
from os import walk
import os.path
import bleach

tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em', 'i', 'h1','h2','h3','h4','h5','h6','h7','hr','li', 'ol', 'pre', 'strong', 'ul']

attr = {'a': ['href', 'title'], 'abbr': ['title'], 'acronym': ['title']}


def convert_html_to_stripped_html(HtmlList):

    if len(HtmlList) == 0:
        return "No html files found"


    print("HTML to Stripped HTML", end="")
    for path in HtmlList:

        print(".", end="")
        pathsplit = path.split("/")

        html_original = open(str(path), "r").read()
        html = bleach.clean(html_original, 
            tags=tags, attributes=attr, strip=True)

        file_name = str(pathsplit[-1])
        file_name = file_name.replace(".htm", ".html")
        f = open(f"output/html/{file_name}", "w")
        f.write(html)
        f.close()

    print()
    return "HTML was stripped (1/4)"

