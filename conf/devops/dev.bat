@rem ------------------- batch setting -------------------
@echo off

@rem ------------------- declare variable -------------------
if not defined PROJECT_ENV (set PROJECT_ENV=cli)

@rem ------------------- execute script -------------------
call :%*
goto end

@rem ------------------- declare function -------------------

:action-prepare
    echo ^> Startup and into container for develop algorithm
    @rem build image
    cd ./conf/docker/asa-api
    docker build -t isa:%PROJECT_NAME% .
    cd %CLI_DIRECTORY%

    @rem create cache
    IF NOT EXIST cache (
        mkdir cache
    )
    goto end

:action-remove
    docker rm -f %DOCKER_CONTAINER_NAME%
    goto end

:action
    @rem declare variable
    set DOCKER_CONTAINER_NAME=isa-%PROJECT_NAME%

    @rem management container
    if defined TARGET_PROJECT_STOP (
        echo Stop project %PROJECT_NAME% develop server
        call :action-remove
    ) else (
        echo Start project %PROJECT_NAME% develop server
        if "%TARGET_PROJECT_COMMAND%"=="bash" (
            echo ^> Into service
            docker exec -ti %DOCKER_CONTAINER_NAME% bash
        ) else (
            echo ^> Startup service
            call :action-prepare
            call :action-remove

            @rem execute container
            docker run -d ^
                -v %cd%\cache\data:/data ^
                -v %cd%\conf\docker\asa-api\cli:/usr/local/asa ^
                -v %cd%\conf\docker\asa-api\api\server:/usr/local/fastapi ^
                -v %cd%\app:/app ^
                -p 8080:80 ^
                --name %DOCKER_CONTAINER_NAME% ^
                isa:%PROJECT_NAME% %TARGET_PROJECT_COMMAND%
        )
    )
    goto end

:args
    set COMMON_ARGS_KEY=%1
    set COMMON_ARGS_VALUE=%2
    if "%COMMON_ARGS_KEY%"=="--stop" (set TARGET_PROJECT_STOP=true)
    if "%COMMON_ARGS_KEY%"=="--into" (set TARGET_PROJECT_COMMAND=bash)
    goto end

:short
    echo Developer mode
    goto end

:help
    echo This is a Command Line Interface with project %PROJECT_NAME%
    echo Startup Server
    echo.
    echo Options:
    echo      --help, -h        Show more information with '%~n0' command.
    echo      --into            Into container when it is at detach mode.
    echo      --stop            Stop container if dev-server was on work.
    call %CLI_SHELL_DIRECTORY%\utils\tools.bat command-description %~n0
    goto end

:end
