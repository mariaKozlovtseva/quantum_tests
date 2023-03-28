@echo off
call env_vars_set

call conda activate %PROJECT_ENV%

setlocal

:: Copy batch script that sets the environment variables to the conda env directory
:: so that it is executed every time the conda env is activated
set ACTIVATE_DIR=%CONDA_PREFIX%\etc\conda\activate.d
if not exist "%ACTIVATE_DIR%" mkdir "%ACTIVATE_DIR%"

set ACTIVATE_BAT=%ACTIVATE_DIR%\env_vars_set.bat
echo Copying env_vars_set.cmd to %ACTIVATE_DIR%
copy /y env_vars_set.cmd "%ACTIVATE_BAT%" >NUL
:: Replace %cd% string with its calculated value (project root directory) in the env script
powershell -Command "(gc \"%ACTIVATE_BAT%\") -replace '%%cd%%', '%cd%' | Out-File -encoding ASCII \"%ACTIVATE_BAT%\""

:: Copy batch script that unsets the environment variables to the conda env directory
:: so that it is executed every time the conda env is deactivated
set DEACTIVATE_DIR=%CONDA_PREFIX%\etc\conda\deactivate.d
if not exist "%DEACTIVATE_DIR%" mkdir "%DEACTIVATE_DIR%"

echo Copying env_vars_unset.cmd to %DEACTIVATE_DIR%
copy /y env_vars_unset.cmd "%DEACTIVATE_DIR%\env_vars_unset.bat" >NUL

:: Create a path configuration file with the path to the project source code in the conda env directory
:: in order to include the src path in the PYTHONPATH every time the conda env is activated
for /f "usebackq tokens=*" %%p in (`python -c "import site; print(site.getsitepackages()[0])"`) do set SIDEPATH=%%p
echo Creating project path configuration file: %SIDEPATH%\%PROJECT_ENV%.pth
echo %cd%\src> "%SIDEPATH%\%PROJECT_ENV%.pth"

:: De-activate the conda environment to apply the changes above
call conda deactivate

call env_vars_unset
