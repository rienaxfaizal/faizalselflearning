# Todoist Mock Automation
Initial framework for scalable automation tests for Todoist App

## Prerequiste 

- [Android Emulator](https://developer.android.com/studio/run/emulator)
- [Appium](http://appium.io/)
- [Python 3](https://www.python.org/) (Code developed in version 3.7)


## Setup

- Clone this repository

    `git clone git@github.com:/rienaxfaizal/faizalselflearning.git`
- Install python dependancies

    `pip install -r requirements.txt`
    
- Launch instance of Android virtual device (API 29)
- Launch appium server (Version 1.18.0) + Port 4723
- Fill in relevant config details in [config file](config.py). This includes Todoist Account Credentials and API Token

## Run Tests
Tests were written using [PyTest](https://docs.pytest.org/en/stable/). 

Run the following command from project root directory

`python -m pytest tests
`

Additional configuration (based on current internet connection)

class BasePage:

    PAGE_LOAD_WAIT = 30
    SYNC_LOAD_TIME = 20

For Each test project (new configuration added)
allow more time to load the pages accordingly

    # TODO: replace with explicit wait
    time.sleep(10)

