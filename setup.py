# setup.py
from setuptools import setup, find_packages

setup(
    name='simple_math_package',
    version='1.0.0',
    packages=find_packages(),
    py_modules=['app'],
    description='Un paquete simple de matemáticas creado para mi demostración de CI/CD.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='[Mi Nombre]',
    license='MIT',
)