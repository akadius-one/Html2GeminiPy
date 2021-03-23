import os
from os import walk
import os.path

def convert_links_to_gemini(domain):

    print("Links to gemini", end="")
    for file in os.listdir("output/gemini"):

        if not file.endswith(".md"):
            continue

        print(".", end="")
        processed = ""
        f = open("output/gemini/" + file, "r")
        for line in f.readlines():
            if ".html" in line and "http" not in line or domain in line:
                line = line.replace("html", "gmi")
                url = line.split(" ")[1]
                
                link = url.split("/")[-1]

                line = line.replace(str(url), str(link))

                processed += line

            else:
                processed += line
        f.close()
        f = open("output/gemini/" + file, "w")
        f.write(processed)
        f.close()

    print()
    return("Links are converted to gemini (4/4)")
