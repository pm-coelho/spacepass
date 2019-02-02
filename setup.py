from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='passmacs',
    version='0.1',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/passmacs',
    description='A spacemacs inspired menu for password store',
    long_description=readme(),
    license='GPLv3+',
    packages=['passmacs'],
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': ['passmacs=passmacs.run:main']
    }
)
