from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='geojson-precision',
      version='0.0.1',
      description=u"Adjust precision of geojson coordinates",
      long_description=long_description,
      classifiers=[],
      keywords='geojson',
      author=u"Matthew Perry",
      author_email='perrygeo@gmail.com',
      url='https://github.com/perrygeo/geojson-precision',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['click', 'cligj', 'shapely'],
      entry_points="""
      [console_scripts]
      geojson-precision=geojson_precision.cli:main
      """
      )
