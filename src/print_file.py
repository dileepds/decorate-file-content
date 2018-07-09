"""

This module has one class which iterating through the input content and parse the content to give a desired
output format

"""
import sys
import re
import textwrap


class print_file(object):
    """
     Class having the functionality to read the input content and write the output
     in desired format.
    
    """
    def __init__(self):
        """
        constructor of the class print_file which initialize the line index values        
        @param self: reference to class instance
        @type self: current instance of the class  
        """
        self.line_num = 0
        self.line_block = []

    def print_content(self):
        """
        This method is used to iterate over the lines read from standard input
        and print the decorated line to standard output
        @param self: reference to class instance
        @type self: current instance of the class
        @param input_string: the string to be manipulated
        @type text: string    

        """
        #Looping through each raw in the standard input
        for line in sys.stdin:
            #skip all empty lines
            if line.strip():
                # parsing each line and printing the decorated line  
                self.parse_line(line)

        if self.line_block:
                self.format_line_block(self.line_block)

    def parse_line(self, line):
        """
        This method will devide the input content into star block
        Form a list which contain all the lines between star lines
        This method also calculate the number of star in the line.
        @param self: reference to class instance
        @type self: current instance of the class
        @param line: the line to be formatted
        @type line: string        

        """
        if line.startswith("*"):
            if self.line_block:
                self.format_line_block(self.line_block)
            #initialize a list when the input line starts with *
            self.line_block = []
            #calculating the number of * in the start of the line
            star_count = len(line) - len(line.lstrip("*"))
            self.format_star_line(line, star_count)            
        else:
            #adding all the lines followed by * line to the list
            self.line_block.append(line)

    def format_star_line(self, line, star_count):
        """
        This method is used to format the line which starts with *
        @param self: reference to class instance
        @type self: current instance of the class
        @param line: input line
        @type line: String
        @param star_count: number of stars in the line
        @type star_count: Integer
        """
        if star_count == 1:
            self.line_num = self.line_num + 1
            self.last_star_count = 1
            self.sub_index_list = [str(self.line_num)]
            self.sub_index = 1
            new_line = line.replace("*", str(self.line_num))
            self.write_to_std_output(new_line.strip())
        else:           
            if self.last_star_count > star_count:
                star_count_index = int(self.sub_index_list[star_count])+1
                self.sub_index_list = self.sub_index_list[:star_count-1]
                self.sub_index_list.append(str(star_count_index))                
            else:
                self.sub_index_list.append(str(self.sub_index))
                
            large_line_lum =  '.'.join(self.sub_index_list)
            self.last_star_count = star_count 
            new_line = re.sub(r"\*+", large_line_lum, line)
            self.write_to_std_output(new_line.strip())      

    def format_line_block(self, line_block):
        """
        This method is used to format the lines after the line starts with *
        Used to replace . with + and - using the logic if the line is foldable or not
        @param self: reference to class instance
        @type self: current instance of the class
        @param line_block: list contain all the lines within a star block
        @type line_block: List
        """
        tabs_to_use = 1
        for index, tag in enumerate(line_block[:-1]):
            dot_count_line1 = len(tag)-len(tag.lstrip('.'))            
            dot_count_line2 = len(line_block[index+1]) -len((line_block[index+1]).lstrip('.'))
            if (dot_count_line2 > dot_count_line1) or (dot_count_line2 == 0) :
                new_line = re.sub(r"\.+", r"+", tag)
                self.indent_line(new_line, tabs_to_use)
                tabs_to_use = tabs_to_use + 1                
            else:
                new_line = re.sub(r"\.+", r"-", tag)
                self.indent_line(new_line, tabs_to_use)

           
        last_line = re.sub(r"\.+", r"-", line_block[-1])
        self.indent_line(last_line, tabs_to_use)

    def indent_line(self, line, tabs_to_use):
        """
        This method is used to indend the lines which starts with .
        @param self: reference to class instance
        @type self: current instance of the class
        @param line: line to be indended 
        @type line: String
        @param tabs_to_use: An integer which can be used to give proper indent space 
        @type tabs_to_use: Integer
        """
        dedented_text = textwrap.dedent(line).strip()
        wrapped = textwrap.fill(dedented_text, initial_indent=(' '*tabs_to_use))
        self.write_to_std_output(wrapped)
   
    def write_to_std_output(self, output):
        """
        This method is used to print the output line
        @param self: reference to class instance
        @type self: current instance of the class
        @param output: the line to be printed to stdout
        @type output: String
        """
        print "{0}".format(output)

if __name__ == '__main__':
    pf = print_file()
    pf.print_content()
