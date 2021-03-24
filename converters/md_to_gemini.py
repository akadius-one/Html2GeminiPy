import os
import os.path
import time

from md2gemini import md2gemini

path_from = "output/markdown"
path_to = "output/gemini"


def convert_md_to_gemini(domain, overwrite=False):

    print("Markdown to Gemini")

    for file_name in os.listdir(path_from):

        if not file_name.endswith(".md"):
            continue

        new_file_name = file_name.replace(".md", ".gmi")
        if os.path.exists(f"{path_to}/{new_file_name}") and not overwrite:
            continue

        print(".", end="")

        tic = time.perf_counter()
        gemini = create_gemini(file_name)
        toc = time.perf_counter()
        print(f"create_gemini time {toc - tic:0.4f} seconds for {file_name}")

        gemini = remove_html(gemini)
        gemini = links_to_gemini(gemini, domain)

        f = open(f"{path_to}/{new_file_name}", "w")
        f.write(gemini)
        f.close()

    print(" Done")


def create_gemini(file_name):

    with open(f"{path_from}/{file_name}", "r") as f:
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

