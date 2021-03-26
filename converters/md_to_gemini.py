import os
import time

from md2gemini import md2gemini
from converters import util

path_from = "output/markdown"
path_to = "output/gemini"


def convert_md_to_gemini(path_list, domain, overwrite=False):
    
    file_outputs = []
    print("Markdown to Gemini")

    for path_input in path_list:

        if not path_input.endswith(".md"):
            continue
        
        file_input = os.path.basename(path_input)
        file_output = os.path.join( path_to, file_input.replace(".md", ".gmi") )
        if overwrite or not util.file_exists(file_output) :
        
            # print(".", end="")
            print(f"- {file_input}")
            
            tic = time.perf_counter()
            gemini = create_gemini(path_input)
            toc = time.perf_counter()
            print(f"create_gemini time {toc - tic:0.4f} seconds for {path_input}")
    
            gemini = remove_html(gemini)
            gemini = links_to_gemini(gemini, domain)
    
            f = open( file_output, "w", encoding="utf-8")
            f.write(gemini)
            f.close()

        file_outputs.append(file_output)

    print(" Done")
    return file_outputs

def create_gemini(path):

    with open(path, "r", encoding="utf-8") as f:
        markdown = f.read()

    return md2gemini(markdown, links="copy")


def remove_html(gemini):

    return gemini.replace("html\n", "")


def links_to_gemini(gemini, domain):

    lines = gemini.split("\n")

    for line_number, line in enumerate(lines):

        if ".html" in line and "http" not in line or domain in line:
            line = line.replace("html", "gmi")

            url = line.split(" ")[1]
            link = url.split("/")[-1]

            lines[line_number] = line.replace(str(url), str(link))

    return "\n".join(lines)

