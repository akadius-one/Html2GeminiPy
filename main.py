import os
import os.path
import sys
import converters.runner


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


def main( output_path, html_list, domain, overwrite ):
    
    converters.runner.run( output_path, html_list, domain, overwrite, True )


if __name__ == "__main__" :
    
    domain = "akademy.uk"  # Fill in your domain or leave untouched if you dont have one!!!
    overwrite = False
    
    input_path = "input"
    input_path = r"D:\temp\gutenberg-htm"
    # dir = r"C:\Users\tzf82424\Projects\mine\Html2GeminiPy\output\utf8"

    output_path = "output"

    # wipe_old()
    
    path_list = get_paths(input_path)
    path_list = sorted(path_list)
    path_list = path_list[:100]
    
    html_list = get_html(path_list)
    
    main(output_path, html_list, domain, overwrite)
