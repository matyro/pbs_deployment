from setuptools import setup

setup(
    name='pbs_deploy',
    version='0.0.1',
    description='Small scripts to deploy different software on pbs cluster system',
    url='https://github.com/matyro/pbs_depolyment',
    author='Dominik Baack',
    author_email='dominik.baack@tu-dortmund.de',
    license='MIT',
    packages=[
        'pbs_deploy',
    ],
    package_data={
    },
    install_requires=[
        'numpy',           # in anaconda
        'datetime',
	'glob',
	'subprocess',
	'shutil',
	'xmltodict',
    ],
   zip_safe=False,
   entry_points={
    'console_scripts': [
        'pbs_commit = pbs_deploy.pbs_commit:main',
    ],
  }
)
