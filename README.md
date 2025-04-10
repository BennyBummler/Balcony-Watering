# Balcony-Watering
Automatic watering system for the balcony including monitoring.

## Development

### Install required build tools
This is essential for compiling C extensions:
```bash
sudo apt install python3-dev python3-pip python3-setuptools python3-wheel build-essential
```

### Create virtual env
Run the following command from the root folder to create a 
[virtual environment](https://www.raspberrypi.com/documentation/computers/os.html#use-pip-with-virtual-environments) 
configuration folder:
```bash
python -m venv env
```

Before you work on a project, run the following command from the root of the project to 
start using the virtual environment:
```bash
source env/bin/activate
```

You should then see a prompt similar to the following:
```
(env) $
```

### Install dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the 
[requirements.txt](requirements.txt)

```
python -m pip install pip-tools
pip-compile
pip install -r requirements.txt
```