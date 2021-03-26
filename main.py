import os
import os.path
import sys
import time

from converters.html_to_md import convert_html_to_md
from converters.md_to_gemini import convert_md_to_gemini
from converters.html_to_stripped_html import convert_html_to_stripped_html
from converters.to_utf8 import convert_to_utf8


def wipe_old():
    
    for root, dirs, files in os.walk("output"):
        for file in files:
            if not file.startswith(".") :
                print( file )
                #os.remove(os.path.join(root, file))

    print("old stuff is gone")


def get_paths(dir):
    PathList = []
    for thing in os.listdir(dir):
        path = os.path.join(dir, thing)
        PathList.append(path)
        try:
            PathList += get_paths(path)
        except:
            pass
    return PathList


def get_html(PathList):
    HtmlList = []
    for path in PathList:
        if ".html" in path or ".htm" in path:
            HtmlList.append(path)
    return HtmlList



domain = "akademy.uk"  # Fill in your domain or leave untouched if you dont have one!!!
overwrite = True

dir = "input"
# dir = r"D:\temp\gutenberg-htm"
# dir = r"C:\Users\tzf82424\Projects\mine\Html2GeminiPy\output\utf8"

path_list = get_paths(dir)
path_list = sorted(path_list)
path_list = path_list[:100]

html_list = get_html(path_list)

# wipe_old()

tic = time.perf_counter()
utf8_list = convert_to_utf8(html_list)
toc = time.perf_counter()
print(f"html_stripped time {toc - tic:0.4f} seconds")

# sys.exit()

tic = toc
stripped_html_list = convert_html_to_stripped_html(utf8_list, overwrite)
toc = time.perf_counter()
print(f"html_stripped time {toc - tic:0.4f} seconds")

tic = toc
md_list = convert_html_to_md(stripped_html_list, overwrite)
toc = time.perf_counter()
print(f"markdown time {toc - tic:0.4f} seconds")

tic = toc
gemini_list = convert_md_to_gemini(md_list, domain, overwrite)
toc = time.perf_counter()
print(f"gemini time {toc - tic:0.4f} seconds")