# c_file_tester
Testing c file output using 'input.txt' and 'correct_output.txt' files.

### Flow:
1. Compile the c file.
2. Run the executable file and create 'output.txt'.
3. Delete the executable file.
4. compare 'correct_output.txt' with 'output.txt'.

### Requirements:
1. If you want the printing to be in colors, you should use a platform that supports 'ANSI color codes'. Most IDEs support it, e.g pycharm.
2. At the start of the file, you should change the value of `c_file_path` to your c file path.
3. At the start of the file, you should change the value of `compiler_path` to the path of "gcc.exe" on your computer.
* If your shell supports the 'gcc' command, check out `line 19` in the code.
4. In the same directory of the python program you should have "input.txt", "correct_output.txt" files.

### Usage:
Let's see how we are testing the c program "calcultor.c" : \
'calcultor.c' should ask for an operator and two numbers. \
The program will print the compatible value and ask the user to enter another expression. \

For example, if the input is:

<img src="https://user-images.githubusercontent.com/92261832/208772935-c9e9e628-5f9f-43bf-b427-0c097d99ebc4.png" width="100" height="auto">

Then the output shuold be:

<img src="https://user-images.githubusercontent.com/92261832/208773130-97d1eb91-c7b6-47c6-824b-9dbf06e59f47.png" width="500" height="auto">

By running our program using pycharm IDE we get:

<img src="https://user-images.githubusercontent.com/92261832/208774078-71a1272f-d3af-4254-9ee6-47f3121ea362.png" width="500" height="auto">

If the two files are not identical, the program will notify us where they differ.

### That's it!
### Create 'input.txt' file for your program and 'correct_output.txt' file for this input and check whether your c program works as it should! 
