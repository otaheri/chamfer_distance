from setuptools import setup

setup(
    name='chamfer_distance',
    packages=['chamfer_distance'],
    include_package_data=True,
    #packages=find_packages(),
    description='An implementation for chamfer distance in pytorch from chrdiller',
    #long_description=open("README.md").read(),
    #long_description_content_type="text/markdown",
    version='0.1',
    url='https://github.com/OmidThr/chamfer_distance',
    author='Omid Taheri, Christian Diller',
    author_email='omid.taheri@tuebingen.mpg.de',
    maintainer='Omid Taheri',
    maintainer_email='omid.taheri@tuebingen.mpg.de',
    keywords=['pip','chamfer_distance'],
    install_requires=['torch>=1.1.0','Ninja'],
      
    )
