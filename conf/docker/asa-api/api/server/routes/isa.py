# Import server libraries
import sys
import os
import io
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from typing import Union

# Import algorithm-service-application command-interface-line pacakge
sys.path.append(os.path.abspath('/usr/local'))
sys.path.append(os.path.abspath('/usr/local/isa'))
os.environ['PYTHON_CLI_DIR']="/usr/local/isa"
os.environ['PYTHON_CLI_NAME']="isa"
from asa import main

# Declare variable
module = FastAPI()

# Declare function
def print2string(func, args=None):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    func(args)
    captured_string = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return captured_string

# Declare FastAPI route
@module.get("/", response_class=PlainTextResponse)
def algorithm_service_command_description():
    captured_string = print2string(main.cli.print_help)
    return f"{captured_string}"

@module.get("/ls", response_class=PlainTextResponse)
def list_all_algorithm():
    args = main.cli.parse_args(["ls"])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.get("/exec/{algorithm_info:path}", response_class=PlainTextResponse)
def execute_algorithm(algorithm_info: str):
    cmd = ["exec"]
    cmd = cmd + algorithm_info.split("/")
    args = main.cli.parse_args(cmd)
    captured_string = print2string(args.func, args)
    return f"{captured_string}"
