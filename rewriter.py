from sys import argv

# rewrites a simple program that adds two variables to add up to 50.
# the result will be a .mPy file of the same name as the input filename
def rewriter(file_name):
   # various correction rules for a possible program that adds two arguments
   correction_rules = ["a + b",
                       "a - a + b", "a - b + b", "a + b - a", "a + b - b", 
                       "a + 1 + b", "a + 2 + b", "a + 3 + b", "a - 1 + b", 
                       "a - 2 + b", "a - 3 + b", "a + b + 1", "a + b + 2", 
                       "a + b + 3", "a + b - 1", "a + b - 2", "a + b - 3"]

   new_filename = file_name.replace("py", "mPy")

   code_text =[]

   with open(file_name, "r") as file_o:
      code_text = file_o.readlines()

   with open(new_filename, "w") as file_w:
      for line in code_text:
         # find 'return' in line to replace
         if "return" in line:
            # double curly braces to make it easier to find for the translator
            rules = "{{"
            
            index = code_text.index(line)
            
            for r in correction_rules:
               rules = rules + r + ", "
            rules = rules[:len(rules)-2] + "}}"   
            code_text[index] = "\treturn " + rules + "\n"
      file_w.writelines(code_text)
   return new_filename

if __name__ == "__main__":
   rewriter(argv[1])