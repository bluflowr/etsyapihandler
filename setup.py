from distutils.core import setup

setup(
    name='etsyapihandler',
    version='0.2',
    packages=['etsyapihandler',],
    license='BSD',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 0.13.2",
        "requests-oauth >= 0.4.1",
    ],
)