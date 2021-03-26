import os

from markdownify import markdownify

from converters import util

path_from = "output/html"
path_to = "output/markdown"


def convert_html_to_md(path_list, overwrite=False):

    file_outputs = []
    
    print("HTML to Markdown")
    for path_input in path_list:

        if not path_input.endswith(".html"):
            continue

        file_input = os.path.basename(path_input)
        path_output = os.path.join(path_to, file_input.replace(".html", ".md") )
        if overwrite or not util.file_exists(path_output):

            # print(".", end="")
            print(f"- {file_input}")
            
            html = open(path_input, "r", encoding="utf-8").read()
            md = markdownify(html, strip=['style'], heading_style="ATX")
    
            f = open(path_output, "w", encoding="utf-8")
            f.write(md)
            f.close()
            
        file_outputs.append(path_output)
        
        

    print(" Done")
    return file_outputs
