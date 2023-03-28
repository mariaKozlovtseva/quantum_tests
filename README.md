# Getting Started

## Environment Setup
Code was tested on Windows machine, in case of different machine, I created bash setup scripts
1. Install [Anaconda with Python 3](https://www.anaconda.com/products/individual)
   or [Miniconda with Python 3](https://docs.conda.io/en/latest/miniconda.html).
2. Run `./env_create` to create `quantum_env` conda environment (make sure that .sh files are executable, if not write `chmod +x {your_filename}.sh`).
3. Update the `quantum_env` further if necessary by running `./env_update`.
4. Activate env by running `conda activate quantum_env` or `source activate quantum_env`

## Task 1
Write `python src\task1\islands_ocean.py`

## Task 2
Write `python src\task2\train.py`
Write `python src\task2\predict.py`

## Task 3
Write `python src\task3\digit_classifier.py --model-name rand --image-id 15` or `python src\task3\digit_classifier.py --model-name rand`
