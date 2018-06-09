class Configuration:
    def __init__(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.1.0'# '6.0'
        self.desired_caps['deviceName'] = 'emulator'#'WKUWGAO7LV9HJFZH'
        #self.desired_caps['app'] = '/Users/andrey.belyaev/Downloads/app-debug-2.13(250515d92)dev-am-2.1.7.2.apk'
        self.desired_caps['appPackage'] = 'com.allgoritm.youla'#'com.avito.android'
        self.desired_caps['appActivity'] = '.AppInitActivity'#'.home.HomeActivity'
        self.desired_caps['automationName'] = 'uiautomator2'
        self.desired_caps['noReset'] = True
        self.desired_caps['noSign'] = True
        self.desired_caps['skipUnlock'] = True