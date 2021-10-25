
# U-net
![Python application](https://github.com/GamayaSpectral/template_ds/workflows/Python%20application/badge.svg)

Project template for Gamaya python projects

## Description

A longer description of your project goes here...

## Setup virtual environment

```console
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

## Make documentation
```console
    python setup.py build_sphinx
```

## Build reports
```console
    python ./setup.py gen_report
```

## Build project
```console
    python setup.py build
```

## install project
```console
    python setup.py install
```

## Test
```console
    python setup.py test
```
Important note: If you run debug session with breakpoints from pycharm, you might need to add "--no-cov" option in additional arguments as described here: https://stackoverflow.com/a/54690848/2697831

## Packaging

Please check that you have edited the file setup.cfg before trying to install

## Note
If you are using the project template, please change the placeholder with your own repo name.
You can use the following command to go faster:
```console
    $ mv ./src/U-net ./src/your_new_repo_name
    $ find . -path ./venv -prune -o -name '*.py' -exec sed -i -e 's/U-net/your_new_repo_name/g' {} \;
    $ find . -path ./venv -prune -o -name '*.cfg' -exec sed -i -e 's/U-net/your_new_repo_name/g' {} \;
    $ find . -path ./venv -prune -o -name '*.yml' -exec sed -i -e 's/U-net/your_new_repo_name/g' {} \;
    $ find . -path ./venv -prune -o -name 'Makefile' -exec sed -i -e 's/U-net/your_new_repo_name/g' {} \;
    $ find . -path ./venv -prune -o -name '*.md' -exec sed -i -e 's/U-net/your_new_repo_name/g' {} \;
```
Alsom think about changing
* the slack channel name inside of .github/workflows/pythonapp.yml
* the link to build pass badge at the very first line of this readme
