# decorate-file-content

# Formatting the content of the file which read over standard input

This script will takes input.txt as input, parses it, and produces output.txt as output.

# Execute the script

You can execute the script as follows

cat data/example.txt | python src/print_file.py > output.txt

# Input data

The datafile 'data/input.txt' is the input file for the script

# Creating source package 

You can create a source package of the code using the following command and can be published or installed.

python setup.py sdist
