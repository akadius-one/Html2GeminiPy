import os
from os import walk
import os.path
from converters.html_to_md import convert_html_to_md
from converters.md_to_gemini import convert_md_to_gemini
from converters.links_to_gemini import convert_links_to_gemini
from converters.html_to_stripped_html import convert_html_to_stripped_html

dir = "input"

def wipe_old():
    return "Nope"
    for root, dirs, files in os.walk("output"):
        for file in files:
            os.remove(os.path.join(root, file))

    return "old stuff is gone"


def get_paths(dir):
    PathList = []
    for thing in os.listdir(dir):
        PathList.append(dir + "/" + thing)
        try:
            PathList += get_paths(dir + "/" + thing)
        except:
            pass
    return PathList

def get_html(PathList):
    HtmlList = []
    for path in PathList:
        if ".html" in path or ".htm" in path:
            HtmlList.append(path)
    return HtmlList


PathList = get_paths(dir)
HtmlList = get_html(PathList)


domain = "akademy.uk" #Fill in your domain or leave untouched if you dont have one!!!

#print(wipe_old())
print(convert_html_to_stripped_html(HtmlList))
print(convert_html_to_md())
print(convert_md_to_gemini())
print(convert_links_to_gemini(domain))
