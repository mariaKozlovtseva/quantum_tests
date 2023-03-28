@echo off
call env_vars_set
call activate %PROJECT_ENV%
call conda env update -n %PROJECT_ENV% -f environment.yml
call env_vars_unset
