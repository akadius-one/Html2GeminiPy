import os.path
import shutil
from chardet.universaldetector import UniversalDetector


path_to = "output/utf8"


def convert_to_utf8(path_list):

    print("To utf-8")
    file_outputs = []
    
    detector = UniversalDetector()
    
    for path_input in path_list:
        
        file_input = os.path.basename(path_input)
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

        file_output = os.path.join(path_to, file_input )
        if encoding in ['utf-8', 'ascii'] :
            
            try:
                shutil.copyfile(path_input, file_output )
            except shutil.SameFileError:
                pass
            
        else:

            with open(path_input, 'rb') as f:
                decoded = f.read()
            
            encoded = decoded.decode(encoding)
            with open(file_output, 'w', encoding="utf-8") as f:
                f.write(encoded)

        file_outputs.append(file_output)

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