from setuptools import setup, find_packages

setup(name='CiscoPy',
      version='0.1',
      description='Python package for configuring Cisco devices',
      author='Github: devinci-it',
      author_email='vince.dev@icloud.com',
      packages=find_packages(),
      install_requires=[
          'netaddr',
      ],
      entry_points={
          'console_scripts': [
              'ciscopy = CiscoPy.app:main'
          ]
      })
