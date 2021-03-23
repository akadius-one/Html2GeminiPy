import os
from os import walk
import os.path
from markdownify import markdownify

path_from = "output/html"
path_to = "output/markdown"
def convert_html_to_md():

    print("HTML to Markdown", end="")
    for file_name in os.listdir(path_from):

        if not file_name.endswith(".html"):
            continue

        print(".", end="")
        html = open(f"{path_from}/{file_name}", "r").read()
        md = markdownify(html, strip=['style'], heading_style="ATX")

        file_name = file_name.replace(".html", ".md")

        f = open(f"{path_to}/{file_name}", "w")
        f.write(md)
        f.close()

    print()
    return "HTML was converted to Markdown (2/4)"
