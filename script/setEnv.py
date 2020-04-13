import os
import subprocess
from sys import platform

def main():

    print("Getting the library path we already have..")
    current_path = os.path.abspath(os.path.dirname(__file__))
    lib_path = current_path + os.path.sep + ".." + os.path.sep + "lib"

    
    print("Setting the environment..")

#system_name = platform.system()

    if platform == 'linux':
        print("OS system is Linux")
        bin_path = lib_path + os.path.sep + "z3-4.8.7-x64-ubuntu-16.04" + os.path.sep + "bin"
        python_path = bin_path + os.path.sep + "python"

        p = subprocess.Popen("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:" + bin_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        retval = p.wait()      

        subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read()

        os.system("export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:" + bin_path)
        os.system("export PYTHONPATH=" + python_path)

    elif platform == 'Windows':
        print("OS system is Windows")
        bin_path = lib_path + os.path.sep + "z3-4.8.7-x64-win" + os.path.sep + "bin"
        python_path = bin_path + os.path.sep + "python"
        os.system("set PATH=%PATH%;" + bin_path)
        os.system("set PYTHONPATH=" + python_path)

    elif platform == 'Darwin':
        print("OS system is OSX")
        bin_path = lib_path + os.path.sep + "z3-4.8.7-osx-10.14.6" + os.path.sep + "bin"
        python_path = bin_path + os.path.sep + "python"
        os.system("export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:" + bin_path)
        os.system("export PYTHONPATH=" + python_path)
    else:
        print("[ERROR] Something is wrong.. no environment variables are set")


if __name__ == "__main__":
    main()

