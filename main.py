from rewriter import rewriter
from translator import mPy_to_sketch
from sys import argv
import subprocess


if __name__ == "__main__":
   try:
      # create the mPy file (.mPy) and store the name
      mPy_name = rewriter(argv[1])

      # create the sketch file (.sk) and store the name
      sk_name = mPy_to_sketch(mPy_name)
      
      # runs sketch on the code.sk code to find the recommended change
      subprocess.run(["./sketch", sk_name])
   except:
      print("Error: Usage is \"py main.py <pythonscripthere>\" (without the quotes)")
      print("If the usage is correct, check if the format of your script is the same as the given example script in code.py")
      print("Also, check if sketch can be run from your default command line")
      print("Otherwise, just remove the part to run sketch and do it manually to get the sketch output")