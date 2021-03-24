import os
from os import walk
import os.path
from markdownify import markdownify

path_from = "output/html"
path_to = "output/markdown"


def convert_html_to_md(overwrite=False):

    print("HTML to Markdown")
    for file_name in os.listdir(path_from):

        if not file_name.endswith(".html"):
            continue
            
        new_file_name = file_name.replace(".html", ".md")
        if os.path.exists(f"{path_to}/{new_file_name}") and not overwrite:
            continue

        print(".", end="")
        html = open(f"{path_from}/{file_name}", "r").read()
        md = markdownify(html, strip=['style'], heading_style="ATX")

        
        f = open(f"{path_to}/{new_file_name}", "w")
        f.write(md)
        f.close()

    print(" Done")
