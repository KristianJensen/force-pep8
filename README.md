# force-pep8
IPython extension for seeing PEP8 errors directly in the notebook.

This module can be loaded as an extension in a Jupyter notebook to get direct feedback on correct coding style.
The notebook will yell at you (thorugh stderr) until you write clean PEP8-compliant code.

Future features:
 - Hardcore mode: An exception will be raised when code is not PEP8-compliant.
 - Super-hardcore mode: Running a cell with non-PEP8-compliant code will restart the kernel and delete a random file on your file system.
 
To load the extension in a notebook run:
```python
%load_ext force_pep8
```
After running a cell you will now see output if the code does not comply to PEP8. To verify that this works you can try to run:
```python
a=3
```
