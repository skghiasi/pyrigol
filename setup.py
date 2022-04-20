from setuptools import setup

setup(
   name='pyrigol',
   version='0.0',
   description='Something different',
   author='kghiasi',
   author_email='skyghiassi@gmail.com',
   url = 'git@gitlab.ewi.tudelft.nl/kghiasi/pyrigol.git'
   packages=['pyrigol'],  # would be the same as name
   install_requires=['pyvisa'], #external packages acting as dependencies
)