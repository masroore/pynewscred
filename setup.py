from setuptools import setup, find_packages

install_requires = ['setuptools']
if sys.version_info < (2, 6):
    install_requires.append('simplejson')  
    
setup(
      name='pynewscred',
      version='0.1.1',
      description='Newscred.com REST API Client',
      author='Dr. Masroor Ehsan',
      author_email='masroore@gmail.com',
      license = 'BSD',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],       
      url='http://www.my.com/',
      keywords="newscred",
      packages=['pynewscred'],
      install_requires = install_requires,
)