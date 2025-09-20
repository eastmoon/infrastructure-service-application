# Import libraries
import sys

# Declare class
class Service:
    ## Declare member variable
    ### Publish
    container = None
    ### Private
    __config = None
    __module = None
    ## Declare constructor
    def __init__(self, config, module):
        self.__config = config
        self.__module = sys.modules[module]
        if 'container' in config:
            self.container = config['container']
        if 'sys.attributes' in config:
            self.container['sys'] = config['sys.attributes'].copy()

    ## Declare member method
    def exec(self):
        if 'container' in self.__config and hasattr(self.__module, 'container'):
            self.__module.container(self, self.__config['container'])
        if 'authorize' in self.__config and hasattr(self.__module, 'authorize'):
            self.__module.authorize(self, self.__config['authorize'])
        if 'secure' in self.__config and hasattr(self.__module, 'secure'):
            self.__module.secure(self, self.__config['secure'])
        if 'command' in self.__config:
            for cmd_object in self.__config['command']:
                match cmd_object['cmd']:
                    case 'template':
                        print(f"Execute : {cmd_object['msg']}")
                        print(f"Do template with {cmd_object['data']}")
                    case 'api':
                        print(f"Execute : {cmd_object['msg']}")
                        print(f"Do RestAPI with {cmd_object['data']}")
                    case 'ssh':
                        print(f"Execute : {cmd_object['msg']}")
                        print(f"Do SSH with {cmd_object['data']}")
                    case _:
                        if hasattr(self.__module, 'command'):
                            self.__module.command(self, cmd_object)
        default_keys = ['module', 'container', 'authorize', 'secure', 'command']
        for key in self.__config:
            if key not in default_keys:
                if hasattr(self.__module, key):
                    target_function = getattr(self.__module, key)
                    target_function(self, self.__config[key])

    ## Declare accessor
    @property
    def config(self):
        return self.__config
