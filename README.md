# force-pep8
IPython extension for seeing PEP8 errors directly in the notebook.

This module can be loaded as an extension in a Jupyter notebook to get direct feedback on correct coding style.
The notebook will yell at you (thorugh stderr) until you write clean PEP8-compliant code.

Future features:
 - Hardcore mode: An exception will be raised when code is not PEP8-compliant.
 - Super-hardcore mode: Running a cell with non-PEP8-compliant code will restart the kernel and delete a random file on your file system.
