# Import libraries
import os
import sys
import re
import glob
import importlib
from conf import attributes

# Declare variable

# Declare function
def conf(parser):
    ## command description
    new_parser = parser.add_parser('list', help='List moduels or show module description.', description=f"List all module in '{attributes.APP_A_DIR}', or give module name to show single module description.")
    ## command options and description
    new_parser.add_argument('module_name', nargs='?', help='Infrastructure module name.')
    ## command process function
    new_parser.set_defaults(func=exec, helper=new_parser.print_help)

def exec(args):
    if args.module_name == None:
        print("Module list:")
        # For recursive search, use '**' and set recursive=True
        ## Search all python file in application directories
        files = glob.glob(f"{attributes.APP_A_DIR}/*.py")
        for file in files:
            file_name = os.path.basename(file)
            algorithm_name = os.path.splitext(file_name)[0]
            show_short(algorithm_name, file)
        ## Search all main.py in application sub-directories
        files = glob.glob(f"{attributes.APP_A_DIR}/*/main.py")
        for file in files:
            folder_path = os.path.dirname(file)
            algorithm_name = os.path.basename(folder_path) # Returns "folder"
            show_short(algorithm_name, file)
    else:
        f_module_path=f"{attributes.APP_A_DIR}/{args.module_name}.py"
        d_module_path=f"{attributes.APP_A_DIR}/{args.module_name}/main.py"
        if os.path.exists(f_module_path):
            show_desc(attributes.APP_A_DIR, args.module_name, args.module_name)
        elif os.path.exists(d_module_path):
            show_desc(f"{attributes.APP_A_DIR}/{args.module_name}", "main", args.module_name)
        else:
            print(f"Error: Module '{args.module_name}' not found at '{attributes.APP_A_DIR}'")

def show_short(algorithm_name, file_path):
    """
    Show module file description base on #@DESC tags.

    Args:
        algorithm_name (str): The algorithm name.
        file_path (str): The algorithm file paths.
    """
    try:
        ## Search #@PARAME , #@DESC tag in algorithm file.
        with open(file_path, 'r') as f:
            print("")
            desc = []
            for line_num, line in enumerate(f, 1):
                if re.search("^#@DESC", line):
                    desc.append(line.split("#@DESC")[1].strip())
        ## Show information with parser result.
        print(f"{algorithm_name}")
        for str in desc:
            print(f" {str}")
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_desc(package_dir, module_file, module_name):
    """
    Show module description with desc function.

    Args:
        package_dir (str): The package path which use to define new system path.
        module_file (str): The module name which use to import.
        module_name (str): The module name.
    """
    try:
        sys.path.append(package_dir)
        module_object = importlib.import_module(module_file)
        if hasattr(module_object, "desc"):
            module_object.desc()
        else:
            print(f"Error: 'desc' function not found in module {module_name}")
    except Exception as e:
        print(f"An error occurred: {e}")
