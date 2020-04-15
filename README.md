# z3-sudoku

Sudoku puzzle using python APIs of Z3

# Prerequisite

 - The Z3 Python API requires libz3.dll/.so/.dylib in the 
    - ``PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH``
    - environment variable and the ``PYTHONPATH`` environment variable needs to point to the ``python`` directory that contains ``z3/z3.py`` (which is at bin/python in our binary releases).
 - Z3 version I have tested was Z3-4.8.7 from https://github.com/Z3Prover/z3/releases


# Running this example on Windows:
 - ``set PATH=%PATH%;MYZ3\bin``
 - ``set PYTHONPATH=MYZ3\bin\python``
 - ``python main.py <input file in txt>``

# Running this example on Linux:
 - ``export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:MYZ3/bin``
 - ``export PYTHONPATH=MYZ3/bin/python``
 - ``python main.py <input file in txt>``

# Running this example on macOS:
 - ``export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:MYZ3/bin``
 - ``export PYTHONPATH=MYZ3/bin/python``
 - ``python main.py <input file in txt>``
