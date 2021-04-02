import os.path

from converters.html_to_md import convert_html_to_md
from converters.md_to_gemini import convert_md_to_gemini
from converters.html_to_stripped_html import convert_html_to_stripped_html
from converters.to_utf8 import convert_to_utf8
from converters.util import timer


def run( output_root_path, html_list, domain, overwrite, timings=False, wait_count=100, wait_length=10 ):

	if timings :
		tic = timer()

	output_path = os.path.join(output_root_path, "utf8")
	utf8_list = convert_to_utf8(output_path, html_list, overwrite, wait_count, wait_length)
	
	if timings:
		tic = timer(tic, "utf8")

	output_path = os.path.join(output_root_path, "html")
	stripped_html_list = convert_html_to_stripped_html(output_path, utf8_list, overwrite, wait_count, wait_length)
	
	if timings:
		tic = timer(tic, "stripped_html")

	output_path = os.path.join(output_root_path, "markdown")
	md_list = convert_html_to_md(output_path, stripped_html_list, overwrite, wait_count, wait_length)
	
	if timings:
		tic = timer(tic, "md")

	output_path = os.path.join(output_root_path, "gemini")
	_gemini_list = convert_md_to_gemini(output_path, md_list, domain, overwrite, wait_count, wait_length)
	
	if timings:
		_tic = timer(tic, "gemini")

