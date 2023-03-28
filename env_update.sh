#!/bin/bash
. ./env_vars_set.sh
source activate $PROJECT_ENV
conda env update -n $PROJECT_ENV -f ./environment.yml
. ./env_vars_unset.sh
