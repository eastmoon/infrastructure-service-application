@rem ------------------- batch setting -------------------
@echo off

@rem ------------------- declare variable -------------------
if not defined PROJECT_ENV (set PROJECT_ENV=cli)

@rem ------------------- execute script -------------------
call :%*
goto end

@rem ------------------- declare function -------------------

:action
    @rem create cache
    echo ^> Create cache directory
    IF NOT EXIST cache (mkdir cache)
    IF EXIST cache\publish (rd /S /Q cache\publish)
    mkdir cache\publish
    mkdir cache\publish\cli
    mkdir cache\publish\api
    mkdir cache\publish\modules

    @rem integrate pack folder
    echo ^> Publish content
    xcopy /Y /S /Q %cd%\conf\docker\isa cache\publish
    xcopy /Y /S /Q %cd%\app\cli cache\publish\cli
    xcopy /Y /S /Q %cd%\app\api cache\publish\api
    xcopy /Y /S /Q %cd%\app\modules cache\publish\modules
    IF EXIST cache\publish\.gitignore (del cache\publish\.gitignore)
    goto end

:args
    goto end

:short
    echo Publish mode
    goto end

:help
    echo This is a Command Line Interface with project %PROJECT_NAME%
    echo Integrate content into publish folder.
    echo.
    echo Options:
    echo      --help, -h        Show more information with '%~n0' command.
    call %CLI_SHELL_DIRECTORY%\utils\tools.bat command-description %~n0
    goto end

:end
