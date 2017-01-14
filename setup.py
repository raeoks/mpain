from setuptools import setup
import mpain

setup(name=mpain.NAME,
      version=mpain.VERSION,
      description=mpain.DESCRIPTION,
      url='http://github.com/raeoks/mpain',
      author='Ranjeet Singh',
      author_email='ranjeet@raeoks.com',
      license='MIT',
      packages=['mpain'],
      install_requires=[],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      entry_points={
          'console_scripts': [
              'mpain = mpain.main:main'
          ],
      },
      zip_safe=False)
