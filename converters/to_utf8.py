import os.path
import shutil

from chardet.universaldetector import UniversalDetector

from converters import util


def convert_to_utf8(path_to, path_list, overwrite=False, wait_count=100, wait_length=10):

    print("To utf-8")
    file_outputs = []
    
    detector = UniversalDetector()

    count = 0
    for path_input in path_list:

        if not path_input.endswith(".htm") and not path_input.endswith("html") :
            continue

        file_input = os.path.basename(path_input)
        path_output = os.path.join(path_to, file_input )
        if overwrite or not util.file_exists(path_output):
            
            print( f"- {file_input}", end="" )
            
            detector.reset()
            with open(path_input, 'rb') as f:
                
                for line in f:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
    
            encoding = detector.result["encoding"]
            print( f" : {encoding}, " + str(detector.result["confidence"]) )
    
            
            if encoding in ['utf-8', 'ascii'] :
                
                try:
                    shutil.copyfile(path_input, path_output )
                except shutil.SameFileError:
                    pass
                
            else:
    
                with open(path_input, 'rb') as f:
                    bytes = f.read()
                
                encoded = bytes.decode(encoding)
                with open(path_output, 'w', encoding="utf-8") as f:
                    f.write(encoded)

            count += 1
            if count % wait_count == 0:
                util.pause(wait_length)

        file_outputs.append(path_output)

    return file_outputs


if __name__ == "__main__" :

    print( "Test" )
    
    files = [
        r"output/utf8/12641-h.htm",
        r"output/utf8/12642-h.htm",
        r"output/utf8/12643-h.htm",
        r"output/utf8/12644-h.htm"
    ]

    convert_to_utf8(files)