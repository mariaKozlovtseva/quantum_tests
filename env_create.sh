#!/bin/bash
. ./env_vars_set.sh

conda env create -n $PROJECT_ENV -f ./environment.yml
source activate $PROJECT_ENV

. ./env_bind.sh > /dev/null
conda deactivate

. ./env_vars_unset.sh
