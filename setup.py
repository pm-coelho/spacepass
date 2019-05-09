from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='spacepass',
    version='0.1',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/spacepass',
    description='A spacemacs inspired menu for password store',
    long_description=readme(),
    license='GPLv3+',
    packages=find_packages(exclude=('test')),
    include_package_data=True,
    install_requires=['spacemenu', 'ConfigArgParse'],
    entry_points={
        'console_scripts': ['spacepass=spacepass.run:main']
    }
)
