# 
sudo apt-get upgrade
sudo apt-get update

# Set up and activate a virtual environment 
python -m venv ~/.venv
source ~/.venv/bin/activate

# install the newest dlt version or upgrade the existing version to the newest one
pip install -U dlt

# install dlt with support for duckdb
pip install "dlt[duckdb]"
# install dlt version smaller than 0.5.0
pip install "dlt<0.5.0"