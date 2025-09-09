# Import libraries
import os
import sys
import re
import json
import yaml
import importlib
from conf import attributes

# Declare class
class Module:
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

class Config:
    ## Declare member variable
    ### Publish
    filename = ""
    path = ""
    ### Private
    _instance = None

    ## Declare constructor
    def __init__(self, filename):
        self.filename=filename
        self.rootPath=f"{attributes.APP_D_DIR}/conf"
        self.path=f"{self.rootPath}/{filename}.yml"
        if not os.path.exists(self.rootPath):
            os.mkdir(self.rootPath)

    ## Declare member method
    def read(self, module: str = "default"):
        """
        Retrieve module content from configuration file.
        If module is 'default', retrieve all configuration content.

        Args:
            module (str): The target module.
        """
        config_data : dict = None
        ## Read configuration file
        config_data = self._load_config()
        ## Show target module or all configuration
        if module == "default":
            print(yaml.dump(config_data, default_flow_style=False))
        elif module in config_data:
            print(yaml.dump(config_data[module], default_flow_style=False))
        else:
            print(f"Error: '{module}' not found in {self.path}.")

    def write(self, module: str = "default", data: str = None, path: str = None):
        """
        Write content with module category in configuration file.
        First, content use data string, otherwise use target file path.

        Args:
            module (str): The target module.
            data (str): The content string.
            path (str): The content file path.
        """
        ## Retrieve input data object
        input_data : dict = None
        config_data : dict = None
        if data != None:
            input_data = self._to_json(data)
            if input_data == None:
                input_data = self._to_yaml(data)
            if input_data == None:
                print(f"Error: STDIN content is unknown format or non valid string.")
        elif path != None:
            root, extension = os.path.splitext(path)
            if extension == ".json":
                input_data = self._load_json(path)
            elif extension == ".yml" or extension == ".yaml":
                input_data = self._load_yaml(path)
            else:
                print(f"Error: File '{path}' is unknown format.")

        ## Read configuration file
        config_data = self._load_config()

        ## Write new configuration into module category
        if input_data != None:
            config_data[module] = input_data

        ## Rewrite configuration file
        with open(self.path, 'w') as file:
            yaml.dump(config_data, file)

    def delete(self, module: str = "default"):
        """
        Remove module in configuration file.

        Args:
            module (str): The target module.
        """
        config_data : dict = None
        ## Read configuration file\
        config_data = self._load_config()
        ## Delete target module
        if module in config_data:
            ## Delete module
            del config_data[module]
            ## Rewrite configuration file
            with open(self.path, 'w') as file:
                yaml.dump(config_data, file)
        else:
            print(f"Error: '{module}' not found in {self.path}.")

    def _to_json(self, data: str):
        """
        Parser a given string to JSON format.

        Args:
            data (str): The string to parser.
        Returns:
            dict: If return None, mean input data is not valid JSON string.
        """
        res = None
        try:
            res = json.loads(data)
        except Exception as e:
            res = None
        return res

    def _to_yaml(self, data: str):
        """
        Parser a given string to YAML format.

        Args:
            data (str): The string to parser.
        Returns:
            dict: If return None, mean input data is not valid YAML string.
        """
        res = None
        try:
            res = yaml.safe_load(data)
        except Exception as e:
            res = None
        return res

    def _load_config(self):
        """
        Load configuration file with 'self.path'.

        Returns:
            dict: If configuration file not exist, parser '{}' string, otherwise return configuration file content.
        """
        if os.path.exists(self.path):
            return self._load_yaml(self.path)
        return yaml.safe_load('{}')

    def _load_json(self, filepath: str):
        """
        Load target file with JSON format.

        Args:
            filepath (str): The target file path.
        Returns:
            dict: If target file load failed, return None, otherwise return target file content.
        """
        res = None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                res = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: File '{filepath}' is not a valid JSON file.")
        except FileNotFoundError:
            print(f"Error: '{filepath}' not found. Please ensure the file exists.")
        except Exception as e:
            print(f"An unexpected error occurred while processing '{filepath}': {e}")
        return res

    def _load_yaml(self, filepath: str):
        """
        Load target file with YAML format.

        Args:
            filepath (str): The target file path.
        Returns:
            dict: If target file load failed, return None, otherwise return target file content.
        """
        res = None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                res = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error: File '{filepath}' is not a valid YAML file: {e}")
        except FileNotFoundError:
            print(f"Error: '{filepath}' not found. Please ensure the file exists.")
        except Exception as e:
            print(f"An unexpected error occurred while processing '{filepath}': {e}")
        return res

    ## Declare accessor
