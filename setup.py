from setuptools import setup, find_packages


version = '1.0.0'

setup(
    name='piBox',
    version=version,
    description='piBox syncs your folder to a RPi without internet',
    # long_description=open('README.rst').read(),
    author='Kaushik Varanasi',
    author_email ='kaushik.varanasi1@gmail.com',
    license='MIT',
    keywords=['Python'],
    url='http://github.com/kaushik94/piBox',
    packages=find_packages(),
    package_data={
        'alex': ['*.gitignore']
    },
    install_requires=[
        'paramiko',
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'piBox=piBox.start:main'
        ],
    }
)