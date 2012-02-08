from nose.plugins.base import Plugin
from Growl import GrowlNotifier, GROWL_NOTIFICATIONS_DEFAULT, Image
from pkg_resources import resource_filename


class Sneazr(Plugin):
    '''
    A Nose plugin which displays Growl notifications
    indicating the number of (un)successful tests.
    '''
    name = 'sneazr'

    def __init__(self):
        '''Registers a Growl notifier.'''
        super(Sneazr, self).__init__()
        # Store resource path to icons in dict.
        self.icon_paths = {}
        for status in ['pass', 'error', 'fail']:
            self.icon_paths[status] = resource_filename(
                'resources', 'logo_%s.png' % status
            )

        app_icon = Image.imageFromPath(
            resource_filename('resources', 'logo.png')
        )
        self.notifier = GrowlNotifier(
            applicationName='Sneazr',
            notifications=GROWL_NOTIFICATIONS_DEFAULT,
            applicationIcon=app_icon
        )
        self.notifier.register()


    def finalize(self, result=None):
        '''
        Checks results of nosetests and prepares
        notification body.
        '''
        if result.wasSuccessful():
            self.__notify(
                'Success!',
                'All tests passed successfully.',
                self.icon_paths['pass']
            )
        elif len(result.errors) > len(result.failures):
            self.__notify(
                'Failure!',
                'Failed with %s errors and %s failures.' % (
                    len(result.errors), len(result.failures)
                ),
                self.icon_paths['error']
            )
        else:
            self.__notify(
                'Failure!',
                'Failed with %s failures and %s errors' % (
                    len(result.failures), len(result.errors)
                ),
                self.icon_paths['fail']
            )


    def __notify(self, title, message, icon_path=None):
        '''
        Sends a Growl notification with the
        given parameters.
        '''
        if icon_path is not None:
            icon = Image.imageFromPath(icon_path)
        else:
            icon = None
        self.notifier.notify(
            GROWL_NOTIFICATIONS_DEFAULT[0],
            title,
            message,
            icon=icon
        )
