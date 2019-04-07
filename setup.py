from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Mock Input',
    url='https://github.com/Sarps/mockinput',
    author='Emmanuel Oppong-Sarpong',
    author_email='esarpong51@gmail.com',
    # Needed to actually package something
    packages=['mockinput'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Mock input for locally testing hackerank or hackerearth challenges before uploading',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)