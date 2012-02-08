from setuptools import setup, find_packages

setup(
    name='sneazr',
    version = '0.1',
    py_modules=['sneaze'],
    author = 'Jesse Miller',
    author_email = 'millerjesse@gmail.com',
    description = 'Have nosetests notify to growl',
    keywords = 'nose tests growl',
    url = 'http://github.com/jessemiller/Sneazr',
    setup_requires=['setuptools-git'],
    tests_require=['nose'],
    install_requires=[
        'nose',
        'py-Growl',
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points = {
        'nose.plugins.0.10': ['sneazr = sneaze:Sneazr']
    }
)
