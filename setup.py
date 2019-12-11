from setuptools import setup

setup(
    name = 'contacts',
    version = '1.0',
    description = 'Contact book through the command line',
    author = 'Roberto Olivera, Robert Ranallo, Aaron Tharp',
    py_modules = ['contacts', 'client'],
    install_requires = ['Click',],
    entry_points = '''
        [console_scripts]
            -h             = contacts:help
            main           = contacts:main
            newContact     = contacts:newContact
            showContacts   = contacts:showContacts
            searchContacts = contacts:searchContacts
        ''',
)
