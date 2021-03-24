import os
import os.path
import time

from converters.html_to_md import convert_html_to_md
from converters.md_to_gemini import convert_md_to_gemini
from converters.html_to_stripped_html import convert_html_to_stripped_html

dir = "input"


# def wipe_old():
#     return "Nope"
#     for root, dirs, files in os.walk("output"):
#         for file in files:
#             os.remove(os.path.join(root, file))
# 
#     return "old stuff is gone"


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

domain = "akademy.uk"  # Fill in your domain or leave untouched if you dont have one!!!
overwrite = False

#print(wipe_old())

tic = time.perf_counter()
convert_html_to_stripped_html(HtmlList, overwrite)
toc = time.perf_counter()
print(f"html_stripped time {toc - tic:0.4f} seconds")

tic = toc
convert_html_to_md(overwrite)
toc = time.perf_counter()
print(f"markdown time {toc - tic:0.4f} seconds")

tic = toc
convert_md_to_gemini(domain, overwrite)
toc = time.perf_counter()
print(f"gemini time {toc - tic:0.4f} seconds")