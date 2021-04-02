from converters.runner import run
from converters.util import file_exists

input_dir = "test/input/"
output_dir = "test/output/"
input_file_names = [
	"131-h",
	"132-h",
]

run( output_dir, [input_dir + f + ".htm" for f in input_file_names], "somewhere.at.somewhere", True, False, 1, 0.1 )

output_files = []
output_files += [output_dir + "utf8/" + f + ".htm" for f in input_file_names]
output_files += [output_dir + "html/" + f + ".html" for f in input_file_names]
output_files += [output_dir + "markdown/" + f + ".md" for f in input_file_names]
output_files += [output_dir + "gemini/" + f + ".gmi" for f in input_file_names]

for of in output_files:
	assert( file_exists(of) is True )

