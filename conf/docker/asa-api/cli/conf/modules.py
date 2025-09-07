# Import libraries
import os
import sys
import re
import importlib
from conf import attributes

# Declare class
class Infrastructure:
    ## Declare member variable
    ### Publish
    package = ""
    filename = ""
    name = ""
    path = ""
    ### Private
    _instance = None

    ## Declare constructor
    def __init__(self, module_name):
        f_module_path=f"{attributes.APP_A_DIR}/{module_name}.py"
        d_module_path=f"{attributes.APP_A_DIR}/{module_name}/main.py"
        if os.path.exists(f_module_path):
            self.package = attributes.APP_A_DIR
            self.filename = module_name
            self.name = module_name
            self.path = f_module_path
        elif os.path.exists(d_module_path):
            self.package = f"{attributes.APP_A_DIR}/{module_name}"
            self.filename = "main"
            self.name = module_name
            self.path = d_module_path
        else:
            print(f"Error: Module '{module_name}' not found at '{attributes.APP_A_DIR}'")

    ## Declare member method
    def short(self):
        """
        Show module file description base on #@DESC tags.
        """
        try:
            ## Search #@PARAME , #@DESC tag in algorithm file.
            with open(self.path, 'r') as f:
                print("")
                desc = []
                for line_num, line in enumerate(f, 1):
                    if re.search("^#@DESC", line):
                        desc.append(line.split("#@DESC")[1].strip())
            ## Show information with parser result.
            print(f"{self.name}")
            for str in desc:
                print(f" {str}")
        except FileNotFoundError:
            print(f"Error: File not found at '{self.path}'")
        except Exception as e:
            print(f"An error occurred: {e}")

    def desc(self):
        """
        Show module description with desc function.
        """
        try:
            sys.path.append(self.package)
            if hasattr(self.instance, "desc"):
                self.instance.desc()
            else:
                print(f"Error: 'desc' function not found in module {self.name}")
        except Exception as e:
            print(f"An error occurred: {e}")

    ## Declare accessor
    @property
    def instance(self):
        if self._instance == None:
            self._instance = importlib.import_module(self.filename)
        return self._instance
