from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='spacepass',
    version='0.3',
    author='pmcoelho',
    author_email='pmcoelho@protonmail.com',
    url='https://github.com/pm-coelho/spacepass',
    description='A spacemacs inspired menu for pass password store',
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='GPLv3+',
    packages=find_packages(exclude=('test')),
    include_package_data=True,
    install_requires=['spacemenu', 'ConfigArgParse'],
    entry_points={
        'console_scripts': ['spacepass=spacepass.run:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: Security'
    ]
)
