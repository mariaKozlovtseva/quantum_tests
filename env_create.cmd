@echo off
call env_vars_set

call conda env create -n %PROJECT_ENV% -f environment.yml
call conda activate %PROJECT_ENV%

call env_bind >NUL
call conda deactivate

call env_vars_unset
