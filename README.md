# HOUSE KEEPING

[![Python application](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml/badge.svg)](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml)

[![codecov](https://codecov.io/gh/guionardo/py-housekeeping/branch/develop/graph/badge.svg?token=v7s2bwquXk)](https://codecov.io/gh/guionardo/py-housekeeping)

[![CodeQL](https://github.com/guionardo/py-housekeeping/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/guionardo/py-housekeeping/actions/workflows/codeql-analysis.yml)


Script for cleaning folders using strategies:

* Maximum number of files in folder
* Maximum occupied space in folder
* Maximum age of files


## Configuration

``` json
[
    {
        "folder": "./fakes/f1",
        "rules": {
            "max_file_count": 100,
            "max_folder_size": 1024000,
            "max_file_age": "1m"
        },
        "action": "delete",
        "action_destiny": "./bkp"
    },
    {
        "folder": "./fakes/f2",
        "rules": {
            "max_file_count": 100,
            "max_folder_size": 1024000,
            "max_file_age": "1d"
        },
        "action": "move",
        "action_destiny": "./fakes/bkp"
    },
    {
        "folder": "./fakes/f3",
        "rules": {
            "max_file_count": 100,
            "max_folder_size": 1024000,
            "max_file_age": "30s"
        },
        "action": "compress",
        "action_destiny": "./fakes/bkp"
    }
]
```
python2 house_keep.py CONFIGURATION_FILE.JSON

## TESTING

* Change time of files [link](https://askubuntu.com/questions/62492/how-can-i-change-the-date-modified-created-of-a-file)
