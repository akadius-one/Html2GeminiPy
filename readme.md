# Html2Gemini

This simple python program allows you to convert html to fully usable gmi files.

Using it is fairly simple:

1. Install md2gemini, markdownify and Bleach with pip before you start.

2. Now place your entire site in the input folder (the script will filter it for html files).

3. Change the "domain" variable to your domain and run main.py with python 3 and wait until it is done. 

You will now find your .gmi files in the output/gemini folder. You can simply run a server with those files and everything should work. This is script is intended to be used on html and text heavy sites. PHP files will not be converted. Codeblocks are somewhat buggy from time to time.
