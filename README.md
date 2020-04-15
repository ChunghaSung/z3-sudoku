Z3-sudoku
---

Python implementation for solving Sudoku puzzle by leveraging python APIs of Z3.

How to run
---
Once you have all settings ready (i.e., Z3 and python), you can simply run ``python src/main.py <input_file.txt>``. 
The example input files are under ``input`` directory. 
Therefore, example running command is ``python src/main.py input/test1.txt``.

Format of input file 
---
The format of input file is each cell should be number from 1 to 9 or "x", with no space for each row.
"x" means the blank you need to fill.
Therefore, one example for enconding for the puzzle is 
```
xxx2857xx
x193xxxxx
x8xxx1x6x
x45x6xxxx
x27xxx14x
xxxx5x68x
x3x9xxx5x
xxxxx347x
xx1528xxx
```

Prerequisite
---
 - The Z3 Python API requires libz3.dll/.so/.dylib in the 
    - ``PATH/LD_LIBRARY_PATH/DYLD_LIBRARY_PATH``
    - environment variable and the ``PYTHONPATH`` environment variable needs to point to the ``python`` directory that contains ``z3/z3.py`` (which is at bin/python in our binary releases).
 - Z3 version I have tested was Z3-4.8.7 from https://github.com/Z3Prover/z3/releases
 - Environment setup on Windows
   - ``set PATH=%PATH%;MYZ3\bin``
   - ``set PYTHONPATH=MYZ3\bin\python``

 - Environment setup on Linux
   - ``export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:MYZ3/bin``
   - ``export PYTHONPATH=MYZ3/bin/python``

 - Environment setup on macOS
   - ``export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:MYZ3/bin``
   - ``export PYTHONPATH=MYZ3/bin/python``
