from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


exts = [
    Extension('cy_simulator',
              ['cy_simulator.pyx'],
              libraries=['m'],
              extra_compile_args=['-ffast-math',
                                  '-fopenmp', '-march=native'],
              extra_link_args=['-fopenmp']
              )]

setup(
    name='cy_simulator',
    cmdclass={'build_ext': build_ext},
    ext_modules=exts,
)
