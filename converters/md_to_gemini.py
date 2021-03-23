import os
from os import walk
import os.path
from md2gemini import md2gemini

def convert_md_to_gemini():

    print( "Markdown to Gemini", end="")

    for file in os.listdir("output/markdown"):

        if not file.endswith(".md"):
            continue

        print(".", end="")
        with open("output/markdown/" + str(file), "r") as f:
            gemini = md2gemini(f.read())
            f.close()

        f = open("output/gemini/" + str(file).replace(".md", ".gmi"), "w")
        f.write(gemini)
        f.close()

    for file in os.listdir("output/gemini"):

        if not file.endswith(".gmi"):
            continue

        print(".", end="")
        processed = ""
        f = open("output/gemini/" + file, "r")
        for line in f.readlines():
            if line == "html\n":
                pass

            else:
                processed += line
        f.close()
        f = open("output/gemini/" + file, "w")
        f.write(processed)
        f.close()

    print()
    return "Markdown was converted to gemini (3/4)"
