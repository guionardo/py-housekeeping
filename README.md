# HOUSE KEEPING

[![Python application](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml/badge.svg)](https://github.com/guionardo/py-housekeeping/actions/workflows/python-app.yml)

[![codecov](https://codecov.io/gh/guionardo/py-housekeeping/branch/develop/graph/badge.svg?token=v7s2bwquXk)](https://codecov.io/gh/guionardo/py-housekeeping)

[![CodeQL](https://github.com/guionardo/py-housekeeping/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/guionardo/py-housekeeping/actions/workflows/codeql-analysis.yml)


Script for cleaning folders using strategies:

* Maximum number of files in folder
* Maximum occupied space in folder
* Maximum age of files

## Usage

### CLI

1. Using a configuration file

```bash
python house_keep.py --config-file /any/setup/folder/house_keep.cfg
```

2. Using CLI commands

```bash
python house_keep.py --folder VALUE --max-age VALUE --max-size VALUE --max-count VALUE --action VALUE --destiny VALUE
```

## Rules

|Option|CLI|Configuration file (JSON)|Example|
|------|---|------------------|---|
|Source Folder|--folder /source/folder|"folder":"/source/folder"|
|Maximum file count|--max-count 100|"rules":{"max_file_count":100}|Keeps only 100 most recent files|
|Maximum folder size|--max-size 1024000|"rules":{"max_folder_size":1024000}|Keeps only most recent files that sums 1024000 bytes|
|Maximum file age (1)|--max-age 60|"rules":{"max_file_age":60}|Keeps only files under 60 seconds of age|
|Maximum file age (2)|--max-age 10m|"rules":{"max_file_age":"10m"}|Keeps only files under 10 minutes of age|
|Action delete|--action delete|"action":"delete"|Delete files from file system|
|Action move|--action move|"action":"move"|Move file to another folder (action destiny)|
|Action compress|--action compress|"action":"compress"|Compress files to zip file and delete them from file system|
|Action destiny|--destiny /destiny/folder|"action_destiny":"/destiny/folder"|Destiny folder for using in 'move' and 'compress' actions|

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


## TESTING

(Depends on pytest and pytest-cov)

Checking coverage

```bash
└─ $ ▶ make test
pytest --cov=src ./
============================= test session starts =============================
platform linux2 -- Python 2.7.18, pytest-4.6.11, py-1.10.0, pluggy-0.13.1
rootdir: /home/guionardo/dev/github.com/guionardo/py-housekeeping
plugins: cov-2.11.1
collected 30 items                                                            

tests/test_action.py ....                                               [ 13%]
tests/test_cli.py ......                                                [ 33%]
tests/test_configuration.py ...                                         [ 43%]
tests/test_file_age.py .........                                        [ 73%]
tests/test_main.py ...                                                  [ 83%]
tests/test_rule.py ..                                                   [ 90%]
tests/test_singleton.py ..                                              [ 96%]
tests/test_utils.py .                                                   [100%]

---------- coverage: platform linux2, python 2.7.18-final-0 ----------
Name                   Stmts   Miss  Cover
------------------------------------------
src/__init__.py            5      0   100%
src/action.py             22      0   100%
src/cli.py               103     25    76%
src/configuration.py      22      0   100%
src/exceptions.py          6      0   100%
src/file_age.py           24      0   100%
src/file_infos.py         46     10    78%
src/folder_config.py      20      2    90%
src/house_keeper.py       89     19    79%
src/logger.py              4      0   100%
src/rule.py               24      0   100%
src/singleton.py          32      2    94%
src/utils.py              21      6    71%
------------------------------------------
TOTAL                    418     64    85%


========================== 30 passed in 1.43 seconds ==========================
```
