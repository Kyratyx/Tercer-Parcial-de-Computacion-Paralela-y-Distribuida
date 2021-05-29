'''
Universidad Sergio Arboleda
Autores: Juan Pablo Mora Aragón
Fecha:Mayo 2021
Computación Paralela y Distribuida
Correo:Juan.mora03@correo.usa.edu.co
'''
from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize
import numpy

exts = (cythonize('cy_heat.pyx', language_level="3", annotate=True))

setup(ext_modules=exts,
    include_dirs=[numpy.get_include()],
    )