# Python ModuleNotFoundError inside a virtual environment

Category: Development

## Symptoms
- ModuleNotFoundError although the package was installed

## Cause
The package was installed in a different Python environment from the one running the script.

## Fix
1. Activate the virtual environment first
2. Check with which python and pip -V
3. Install with python -m pip install package
4. Record dependencies in requirements.txt
