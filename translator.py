from sys import argv

def mPy_to_sketch(filename):
   # read the mPy file for the changes to create a sketch file for
   with open(filename, "r") as mPy_file:
      mPy_text = mPy_file.readlines()

      # list to hold all the variable assignments in the "main" program
      var_assigns = []

      for text in mPy_text:
         # the return at the mPy script should have all the possible corrections to make, so 
         # we create a list of all those corrections to eventually change to
         # match sketch script syntax
         if "return" in text:
            returns = text.strip().strip("return").strip().strip("{}").split(", ")
         # finds the function definition to use for translating into sketch script syntax
         elif "def" in text:
            def_name = text.split("def")[1]
         # finds the assignments to change to match sketch script syntax
         elif " = " in text:
            var_assigns.append("\tint " + text.strip() + ";\n")
         elif "==" in text:
            assertion = "assert" + text.strip().lstrip("if").rstrip(":") + ";"
            
      
   sk_filename = filename.replace("mPy", "sk")
   with open(sk_filename, "w") as sk_file:
      # Used for the if statements for the conditional changes
      ifs = "\tif(??){\n\t\treturn "
      
      # puts the types for the arguments and function (first line of the sketch script)
      def_name = def_name.replace("a", "int a").replace("b", "int b").replace(":"," {").lstrip()
      
      # a list of the lines in the new sketch script file
      new_code_lines = [def_name]

      # creates the "if(??)...return ___" statements and appends to the list of sketch script lines
      for r in returns:
         text = ifs + r + ";\n\t}\n"
         new_code_lines.append(text)
      
      # create "main" for assertion
      new_code_lines.append("}\n\nharness void main(){\n")

      for assigns in var_assigns:
         new_code_lines.append(assigns)
      
      new_code_lines.append(assertion + "\n}")

      sk_file.writelines(new_code_lines)
      
   return sk_filename