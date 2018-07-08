"""

This module has two classes. One class is used to define the decorator.
Other class iterating through the input content and use the decorator class
to print the input content in desired format.

"""
import sys
import re

class wrap_file_format(object):
  """
  Wrap a function to print line in the input file in defined format..
  This class can be used as a decorator to a function.

  Example:

  @wrap_file_format()
  def write_hi(str):
    print str

  """

  def __init__(self):

      """
      constructor of the class wrap_file_format.
      @param self: reference to class instance
      @type self: current instance of the class

      """
      pass

  def __call__(self, func):
      """
      Overriding the default function call operator of the class
      @param self: reference to class instance
      @type self: current instance of the class
      @param func: function object which is to be modified
      @type func: object

      """

      def func_wrapper(self, line):
          """
          Defining the main decorator function to print each line in desired format
          @param self: reference to class instance
          @type self: current instance of the class
          @param line: the string to be decorated
          @type line: String

          """
          new_line = line 
          if (line.startswith('*')) and (line.count("*") == 1):
              self.line_num = self.line_num+1
              new_line = line.replace("*", str(self.line_num))

          elif (line.startswith('**')) and (line.count("*") == 2):
              self.second_index = self.second_index + 1
              self.third_index = 0
              new_line = line.replace("**", str(self.line_num)+"."+str(self.second_index))

          elif (line.startswith('***')) and (line.count("*") == 3):
              self.third_index = self.third_index + 1
              self.fourth_index = 0
              new_line = line.replace("***", str(self.line_num)+"."
                         +str(self.second_index)+"."+str(self.third_index))

          elif (line.startswith('****')) and (line.count("*") == 4):
              self.fourth_index = self.fourth_index + 1              
              new_line = line.replace("****", str(self.line_num)+"."
                         +str(self.second_index)+"."+str(self.third_index)+"."+str(self.fourth_index))

          elif (line.startswith('.') and (line.count(".") == 1)):
              new_line = line.replace(".", "+")

          elif (line.startswith('.') and (line.count(".") > 1)):
              new_line = re.sub(r"\.+", r"-", line)
              
          return "{0}".format(func(self, new_line))
          
      return func_wrapper



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
        self.second_index = 0
        self.third_index = 0

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
                decorated_line =  self.parse_line(line)
                print decorated_line

    @wrap_file_format()
    def parse_line(self, line):
        """
        This method is decorated by wrap file format 
        @param self: reference to class instance
        @type self: current instance of the class
        @param line: the line to be formatted
        @type text: string        
        @return : string which is decorated using a decorator
        @rtype : String

        """
        return line

if __name__ == '__main__':
    pf = print_file()
    pf.print_content()
