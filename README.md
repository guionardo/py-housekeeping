# HOUSE KEEPING

[![Python application](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml/badge.svg)](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml)

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