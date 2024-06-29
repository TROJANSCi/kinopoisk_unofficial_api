from setuptools import setup, find_packages


setup(
    name='kinopoisk_unofficial_api',
    version='1.0',
    package_dir={'': 'src'},
    packages=find_packages('src', include=['kinopoisk_unofficial_api']),
    url='',
    license='',
    author='TROJANSCi',
    author_email='log.maksa@gmail.com',
    description='Asynchronous library for working with https://kinopoiskapiunofficial.tech',
    install_requires=[
        'aiohttp',
        'pydantic'
    ],
)
