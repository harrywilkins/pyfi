from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='pyfi',
      version='0.1',
      description='An advanced module for Python',
      url='https://github.com/harrywilkins/pyfi',
      long_description=readme(),
      author='The Glynns',
      author_email='-',
      license='MIT',
      packages=['pyfi'],
      zip_safe=False)
