from flake8.run import check_code
import sys
from six.moves import StringIO


codes_to_ignore = [
    "W292"
]


def filter_flake8_output(output, error_codes):
    """
    Filters out lines from the flake8 output containing the given error codes.
    """
    filtered_output_list = []
    for line in output.split("\n"):
        if line.startswith("stdin:"):  # Remove the bit saying the the error is in stdin
            line = line[6:]
        for code in error_codes:
            if code in line:
                break
        else:
            filtered_output_list.append(line)
    return "\n".join(filtered_output_list)


def filter_magic_lines(code):
    """
    Remove lines starting with %, in order to not run flake8 on IPython magics
    """
    filtered_lines = []
    for line in code.split("\n"):
        if line.startswith("%"):
            pass
        else:
            filtered_lines.append(line)
    return "\n".join(filtered_lines)


def check_cell_code(code, test=False):
    """
    The function that checks the code in a cell
    """
    code = filter_magic_lines(code)  # Ignore magics

    # Substitute stdout and catch with a StringIO
    old_stdout = sys.stdout
    my_stdout = StringIO()
    sys.stdout = my_stdout

    # Do the flake8 check
    check_code(code)

    # Replace the old stdout
    sys.stdout = old_stdout
    output = my_stdout.getvalue()

    # Remove error messages that should be ignored
    output = filter_flake8_output(output, codes_to_ignore)

    # Write the error to stderr
    if test is False:
        sys.stderr.write(output)
    return output

