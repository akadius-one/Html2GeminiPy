import os
import time

from markdownify import markdownify

from converters import util


def convert_html_to_md(path_to, path_list, overwrite=False, wait_count=100, wait_length=10):

    file_outputs = []
    print("HTML to Markdown")

    count = 0
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
            
            count += 1
            if count % wait_count == 0:
                util.pause(wait_length)
        
        file_outputs.append(path_output)

    print(" Done")
    return file_outputs
