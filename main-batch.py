import os
import os.path
import converters.runner


def main_batch( output_path, input_root, domain, overwrite ):

    html_files = []
    batch = 200
    batch_count = 0
    for root, dirs, files in os.walk(input_root):
        for file in files:

            if file.endswith(".htm") or file.endswith(".html") :
                html_files.append(os.path.join(root, file))
    
                if len(html_files) == batch :
                    
                    batch_count += 1
                    print("BATCH" + str(batch_count) )
                    
                    converters.runner.run( output_path, html_files, domain, overwrite, True )
                    html_files = []


if __name__ == "__main__" :
    
    domain = "akademy.uk"  # Fill in your domain or leave untouched if you dont have one!!!
    overwrite = False

    output_path = "output"
    input_root = "input"

    main_batch(output_path, input_root, domain, overwrite)

