import re
import os.path

import bleach

from converters import util

tags = [
    'a',
    'abbr',
    'acronym',
    'b',
    'blockquote',
    'big',
    'br',
    'code',
    'em',
    'i',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7',
    'hr',
    'li',
    'ol',
    'pre',
    'strong',
    'style',
    'ul'
]

attr = {
    'a': ['href', 'title', 'name', 'alt'],
    'abbr': ['title'],
    'acronym': ['title'],
    'style': ['type']
}


def convert_html_to_stripped_html(path_to, path_list, overwrite=False, wait_count=100, wait_length=10):

    print("*Convert to Stripped HTML")
    
    file_outputs = []
    if len(path_list) == 0:
        return file_outputs

    count = 0
    for path in path_list:

        if not path.endswith(".htm") and not path.endswith("html") :
            continue

        file_name = os.path.basename(path)
        file_output = os.path.join(path_to, file_name.replace(".htm", ".html") )

        if overwrite or not util.file_exists(file_output) :
                    
            #print(".", end="")
            print(f"- {file_name}")
    
            html_original = open(str(path), "r", encoding="utf-8").read()
    
            html = remove_head(html_original)
            html = bleach.clean(
                html,
                tags=tags,
                attributes=attr,
                strip=True,
                strip_comments=True
            )
            html = replace_br(html)
            html = replace_hr(html)
            html = remove_heading_newlines(html)
            
            f = open(file_output, "w", encoding="utf-8")
            f.write(html)
            f.close()
            
            count += 1
            if count % wait_count == 0:
                util.pause(wait_length)
                
        file_outputs.append(file_output)

    print(" Done")
    return file_outputs


def remove_head(html):

    start = re.search("<head>", html, re.IGNORECASE)
    end = re.search("</head>", html, re.IGNORECASE)

    if start:
        start = start.span()[0]

    if end:
        end = end.span()[1]

        if not start:
            start = 0
        
        html = html[:start] + html[end:]
        
    return html


def replace_br(html):
    return html.replace("<br/>", "\r\n").replace("<br>", "\r\n")


def replace_hr(html):
    return html.replace("<hr/>", "-"*30 ).replace("<hr>", "-"*30 )


def remove_heading_newlines(html):
    
    h_max = 7
    
    for h_num in range(1, h_max):
        
        pos = 0
        last = 0
        html_sep = []
        
        h = "h" + str(h_num)
        h_open = re.compile( re.escape(f"<{h}>") )
        h_close = re.compile( re.escape(f"</{h}>") )

        start = h_open.search( html, pos )
        
        while start is not None :
            
            start = start.span()[1]
            pos = start

            end = h_close.search( html, pos )
            
            if end is not None :
                pos = end.span()[1]
                end = end.span()[0]
        
                heading = html[start:end]
                heading = heading.replace("\r", "")
                heading = heading.replace("\n", "")

                html_sep.append(html[last:start])
                html_sep.append(heading)
                html_sep.append(html[end:pos])

            last = pos
            start = h_open.search( html, pos )

        html_sep.append(html[last:])
        
        html = "".join(html_sep)
        
    
    return html


if __name__ == "__main__" :
    
    print( "Test" )
    
    print( remove_heading_newlines("<h1>Hrlle</h1>") )
    print( remove_heading_newlines("<body><h1>Hrlle</h1>SOMEewfwef </body>") )
    print( remove_heading_newlines("<h1>Hr\n\rlle</h1>") )
    print( remove_heading_newlines("<body><h1>Hr\r\nlle\r\n</h1>SOME<h3>Hr\r\nlle\r\n</h3>ewfwef </body>") )
    
