import subprocess
import os

# If the file is not on the same directory - you should give the abs path.
c_file_path = 'calculator.c'

# Specify the full path to the C compiler executable
compiler_path = "C:\\Program Files\\mingw-w64\\x86_64-8.1.0-posix-seh-rt_v6-rev0\\mingw64\\bin\\gcc.exe"


def compile_c_file(c_file):
    # In our example: 'calculator.c' becomes 'calculator.out'
    exe_path = c_file[:-1] + "out"
    print(f"Compiling \033[92m{c_file} \033[0mto \033[92m{exe_path}\033[0m ...")

    # Call the C compiler to compile the C file
    subprocess.run([compiler_path, c_file, "-o", exe_path])

    # If you can use the command 'gcc' in the Shell you can change it to:
    # subprocess.run(['gcc', c_file, "-o", exe_path], shell=True)

    print(f"\033[92m{exe_path}\033[0m was created successfully.\n")
    return exe_path


def run_runnable_file(exe_path):
    print(f"Running \033[92m{exe_path}\033[0m ...")

    # run the C program with 'input.txt' as input and redirect its output to 'output.txt'
    with open('input.txt') as input_file, open('output.txt', 'w') as output_file:
        subprocess.run([exe_path], stdin=input_file, stdout=output_file)

    print(f"\033[92moutput.txt\033[0m was created successfully.\n")


def delete_file(file):
    print(f"Deleting \033[92m{file}\033[0m ... ")

    if os.path.exists(file):
        os.remove(file)
        print(f"\033[92m{file}\033[0m was deleted successfully.\n")
    else:
        print(f"\033[91m{file}\033[0m does not exist.\n")


def compare(text_file_1, text_file_2):
    if not os.path.exists(text_file_1):
        print(f"Missing {text_file_1} file!")
        exit(-1)

    if not os.path.exists(text_file_2):
        print(f"Missing {text_file_2} file!")
        exit(-1)

    print(f"Comparing \033[92m{text_file_1} \033[0mand \033[92m{text_file_2}\033[0m ...")

    # read in the contents of the two files
    with open(text_file_1) as f1, open(text_file_2) as f2:
        file1_contents = f1.read()
        file2_contents = f2.read()

    # check if the files are identical
    if file1_contents == file2_contents:
        print(f"\033[94m{text_file_1}\033[0m and \033[94m{text_file_2}\033[0m are identical!")
    else:
        print("The files are not identical. Here are the differences:")

        # use a difflib to show the differences
        from difflib import Differ
        d = Differ()
        diff = d.compare(file1_contents.splitlines(keepends=True), file2_contents.splitlines(keepends=True))
        print(''.join(diff))


def create_output_file(c_file):
    if not os.path.exists('input.txt'):
        print("Missing input.txt file!")
        exit(-1)

    exe_path = compile_c_file(c_file)
    run_runnable_file(exe_path)
    delete_file(exe_path)


def main():
    if not os.path.exists(c_file_path):
        print(f"C file path was inserted incorrectly. got \033[91m'{c_file_path}'\033[0m")
        exit(-1)
    create_output_file(c_file_path)
    compare('output.txt', 'correct_output.txt')


if __name__ == "__main__":
    main()
