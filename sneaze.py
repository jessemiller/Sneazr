from nose.plugins.base import Plugin
from Growl import GrowlNotifier, GROWL_NOTIFICATIONS_DEFAULT

class Sneazr(Plugin):
    name = 'sneazr'
     
    def __init__(self):
        Plugin.__init__(self)
        self.notifier = GrowlNotifier(applicationName='Sneazr', notifications=GROWL_NOTIFICATIONS_DEFAULT)
        self.notifier.register()
    
    def finalize(self, result=None):
            
        if result.wasSuccessful():
            self.__notify('Success!', 'All tests passed successfully.')
        else:
            self.__notify('Failure!', 'Failed with %s failures and %s errors' % (len(result.failures), len(result.errors)))
                        
        
    def __notify(self, title, message):
        self.notifier.notify(GROWL_NOTIFICATIONS_DEFAULT[0], title, message)
