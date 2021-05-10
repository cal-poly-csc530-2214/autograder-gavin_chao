# autograder-gavin_chao

In this assignment, I had some trouble finding Sketch since most Google searches seemed to return various software that can be used for drawing. Once I did find a Sketch tarball to install with, there were multiple packages I was missing to install Sketch. I had the most trouble getting Bison installed since it also required m4, but I had trouble installing that as well. I eventually got Sketch working once I installed an Ubuntu terminal into my Windows machine and used "sudo apt-get install..." for the various packages that were difficult to find and install from the internet.

The actual work I did on this assignment includes creating some Python scripts to convert a simple addition function into an .mPy file, which would then be converted into a .sk file to run Sketch with. I would have liked to create a more general solution for the Program Rewriter and Sketch Translator, but I was running out of time for this project and ended up writing scripts that were mostly compatible for the example code I wrote in "code.py" that should be included in this GitHub repo.

When testing the Sketch scripts, I found that there wasn't really much difference in runtime to find the problems in the code. Perhaps my implementation was too simple so the differences between using the first solution in the list of corrections and something later down the list wasn't going to be easily apparent. A more complicated program (with more errors to fix) would have likely shown a bigger increase in the Sketch solver runtime.

Images for these runs are also included in this repo
Example Runtimes for add(a, b) == 5: 

1 a = 0, b = 5: Total time = 759
2 a = 0, b = 5: Total time = 996

1 a = 1, b = 5: Total time = 1007
 
1 a = 6, b = 5: Total time = 833
2 a = 6, b = 5: Total time = 845
3 a = 6, b = 5: Total time = 799

If I were to re-visit this assignment, I would have added some way to provide more human readable feedback that would be appropriate for students. I would have also looked to create a more general approach to my Program Rewriter and Sketch Translator that would not adhere too much to the structure of my "code.py" example code. Moreover, I would have tried to implement different kinds of arithmetic as well instead of just an addition function.