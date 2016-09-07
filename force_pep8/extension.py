from force_pep8.check_code import check_cell_code


def wrapper_factory(old_run_cell):
    """
    Create a wrapper function that checks code before executing it
    """
    def run_cell_wrapper(code, *args, **kwargs):
        check_cell_code(code)
        old_run_cell(code, *args, **kwargs)
    return run_cell_wrapper


def load_ipython_extension(shell):
    '''
    Substitutes the IPython run_cell function with a wrapper that also does
    the flake8 check
    '''
    shell._real_run_cell_without_pep_check = shell.run_cell
    shell.run_cell = wrapper_factory(shell.run_cell)


def unload_ipython_extension(shell):
    '''Replace the real IPython run_cell function'''
    shell.run_cell = shell._real_run_cell_without_pep_check
