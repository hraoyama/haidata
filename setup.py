from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='haidata',
    url='https://github.com/hraoyama/haidata',
    author='Hans Roggeman',
    author_email='hansroggeman2@gmail.com',
    # Needed to actually package something
    packages=['haidata'],
    # Needed for dependencies
    install_requires=['numpy','pandas','pytest','jsonpickle>=1.0','json>=2.0.0','traceback','logging','datetime','ftfy','distutils'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='BSD 3-Clause License',
    description='Configurable chainable modules for pandas DataFrame cleaning with persistance',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)