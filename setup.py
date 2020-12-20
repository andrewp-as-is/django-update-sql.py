import setuptools

setuptools.setup(
    name='django-update-sql',
    version='2020.12.21',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
