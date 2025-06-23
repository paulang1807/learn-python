## Virtual Environments
- Requires an active python environment installed on the system
- Packages installed in the virtual environment will not affect the global Python installation 
- Virtualenv does not create every file needed to get a whole new python environment
    - Uses links to global environment files instead in order to save disk space end speed up your virtualenv. 

### Using Inbuilt Python "venv"
```bash
# create the environment
# python -m venv <virtual_env_name>
python -m venv my-venv
# The above creates a folder with the name of the virtual environment
# The directory is created in the location from where the above command is run and contains all relevant folders and files for the virtual environment

# Activate the environment
source my-venv/bin/activate
# Deactivate the environment
deaactivate

# Remove an env 
# Delete the virtual env folder
rm -r my-venv
```

### Using virtualenv
```bash
# Install virtualenv
pip install virtualenv

# create the environment
# virtualenv <path_to_virtual_env_folder>
virtualenv ./my-venv
# The above creates a folder with the name of the virtual environment

# Activate the environment
source ./my-venv/bin/activate
# Deactivate the environment
deaactivate
```

### Using Anaconda
```bash
# Create the environment
# conda create -n <virtual_env_name> <space separated package names to be installed>
conda create -n my-venv python=3 matplotlib
# The above creates a folder with the name of the virtual environment
# The directory is created under anaconda/envs folder and contains all relevant folders and files for the virtual environment

# Activate the environment
source activate my-venv
# Deactivate the environment
conda deaactivate

# View all environments
conda env list 
conda info --envs

# View all packages in an environment that is inactive
conda list -n mids-venv
# View all packages in an environment that is active
conda list 

# Clone an env
conda create --name my-clone --clone my-venv
# Clone the base
conda create --name my-clone --clone base

# Remove an env 
conda remove --name myenv --all
conda env remove -n myenv
```

!!! tip "Install Packages with requirements.txt"
    - Create a file called requirements.txt and add all the package names in that file
    - Install packages
        ```bash
        pip install -r requirements.txt
        ```
