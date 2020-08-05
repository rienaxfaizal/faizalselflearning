import os


class Config:
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APPIUM_HOST = "http://localhost:4723/wd/hub"
    ANDROID_TODOIST_CAPS = {
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Pixel 2 API 30",
        "automationName": "uiautomator2",
        "app": os.path.abspath(ROOT_DIR+'/todoist/apk/com.todoist_15.0.4-6030_minAPI21(nodpi)_apkmirror.com.apk'),
        "appPackage": "com.todoist",
        "appActivity": ".activity.HomeActivity",
      }

    TODOIST_EMAIL = 'rienaxfaizal@gmail.com'
    TODOIST_PASSWORD = 'H@sif12345'
    TODOIST_TOKEN = '27b12f71b9077fdc91b2bb93777b4f8c975d023f'
