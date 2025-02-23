from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    #return list of requirements
    requirements = []
    
    hyphen_e_dot = '-e .'

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements

setup(
    name='ml project',
    version='0.0.1',
    author='Adil',
    author_email='adilzafarrr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)