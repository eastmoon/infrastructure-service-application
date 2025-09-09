# Import server libraries
import sys
import os
import io
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from typing import Union

# Import algorithm-service-application command-interface-line pacakge
sys.path.append(os.path.abspath('/usr/local'))
sys.path.append(os.path.abspath('/usr/local/isa'))
os.environ['PYTHON_CLI_DIR']="/usr/local/isa"
os.environ['PYTHON_CLI_NAME']="isa"
from isa import main

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

@module.get("/list", response_class=PlainTextResponse)
def list_all_modules():
    args = main.cli.parse_args(["list"])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.get("/list/{module_name}", response_class=PlainTextResponse)
def show_module_description(module_name: str):
    args = main.cli.parse_args(["list", module_name])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.get("/conf", response_class=PlainTextResponse)
def list_all_configuration_file():
    args = main.cli.parse_args(["conf", "--methods", "list"])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.get("/conf/{config_filename}", response_class=PlainTextResponse)
def show_configuration_file_content(config_filename: str):
    args = main.cli.parse_args(["conf", "--methods", "get", "--filename", config_filename])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.get("/conf/{config_filename}/{module_name}", response_class=PlainTextResponse)
def show_configuration_file_content(config_filename: str, module_name: str):
    args = main.cli.parse_args(["conf", "--methods", "get", "--filename", config_filename, "--module", module_name])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.post("/conf/{config_filename}/{module_name}", response_class=PlainTextResponse)
async def update_configuration_file_content(config_filename: str, module_name: str, request: Request):
    binary_body = await request.body()
    body = binary_body.decode("utf-8")
    sys.stdin = io.StringIO(body)
    args = main.cli.parse_args(["conf", "--methods", "post", "--filename", config_filename, "--module", module_name, "-i"])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"

@module.delete("/conf/{config_filename}/{module_name}", response_class=PlainTextResponse)
def show_configuration_file_content(config_filename: str, module_name: str):
    args = main.cli.parse_args(["conf", "--methods", "del", "--filename", config_filename, "--module", module_name])
    captured_string = print2string(args.func, args)
    return f"{captured_string}"
