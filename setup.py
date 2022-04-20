from setuptools import setup , find_packages

setup(
   name='pyrigol',
   version='0.0',
   description='Something different',
   author='kghiasi',
   author_email='skyghiassi@gmail.com',
   url = 'git@gitlab.ewi.tudelft.nl/kghiasi/pyrigol.git',
   packages=find_packages(), 
   install_requires=['pyvisa'], #external packages acting as dependencies
)