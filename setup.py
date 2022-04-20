from setuptools import setup

setup(
   name='pyrigol',
   version='2.0',
   description='Something different',
   author='kghiasi',
   author_email='skyghiassi@gmail.com',
   packages=['pyrigol'],  # would be the same as name
   install_requires=['pyvisa'], #external packages acting as dependencies
)