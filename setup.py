from setuptools import setup

setup(
    name = 'contacts',
    version = '0.1',
    description = 'Contact book through the command line',
    author = 'Roberto Olivera, Robert Ranallo, Aaron Tharp',
    py_modules = ['contacts'],
    install_requires = ['Click',],
    entry_points = '''
        [console_scripts]
            -h             = contacts:help
            newContact     = contacts:newContact
            showContacts   = contacts:showContacts
            searchContacts = contacts:searchContacts
            removeContact  = contacts:removeContact
            updateContact  = contacts:updateContact
        ''',
)
