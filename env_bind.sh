#!/bin/bash
. ./env_vars_set.sh
source activate $PROJECT_ENV

# Copy bash script that sets the environment variables to the conda env directory
# so that it is executed every time the conda env is activated
ACTIVATE_DIR="$CONDA_PREFIX/etc/conda/activate.d"
echo Copying env_vars_set.sh to $ACTIVATE_DIR
mkdir -p "$ACTIVATE_DIR" && cp -f ./env_vars_set.sh "$ACTIVATE_DIR"
# Replace `pwd` string with its calculated value (project root directory) in the env script
sed -i 's?`pwd`?"'`pwd`'"?' "$ACTIVATE_DIR"/env_vars_set.sh

# Copy bash script that unsets the environment variables to the conda env directory
# so that it is executed every time the conda env is deactivated
DEACTIVATE_DIR="$CONDA_PREFIX/etc/conda/deactivate.d"
echo Copying env_vars_unset.sh to $DEACTIVATE_DIR
mkdir -p "$DEACTIVATE_DIR" && cp -f ./env_vars_unset.sh "$DEACTIVATE_DIR"

# Create a path configuration file with the path to the project source code in the conda env directory
# in order to include the src path in the PYTHONPATH every time the conda env is activated
SIDEPATH="$(python -c 'import site; print(site.getsitepackages()[0])')"
echo Creating project path configuration file: $SIDEPATH/$PROJECT_ENV.pth
echo "`pwd`/src" > "$SIDEPATH/$PROJECT_ENV.pth"

# De-activate the conda environment to apply the changes above
conda deactivate

. ./env_vars_unset.sh
