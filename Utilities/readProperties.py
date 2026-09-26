import configparser
config=configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')
class Readconfig:
    @staticmethod
    def getAppUrl():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def getUserEmail():
        userName = config.get('common info', 'user_email')
        return userName

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password