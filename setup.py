from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(path:str)->List[str]:
    requirements = []
    with open(path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\t','') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='housing_price',
    version='0.0.1',
    author='hau`',
    author_email='tranquochao0102@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
)