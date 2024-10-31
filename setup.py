from setuptools import setup, find_packages
from typing import List

HYPEN_DOT_E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the requirements.txt file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements

setup(
    name='Deployement',                    # Name of your package
    version='0.0.1',                      # Version of your package
    author='Sindhu',                   # Author's name
    author_email='sindhupriya.k01@gmail.com',# Author's email
    description='Model Deployement',    # Short description of the package
    long_description=open('README.md').read(),  # Detailed description, often from README
    packages=find_packages(),             # Automatically finds and includes all packages
    install_requires=get_requirements('requirements.txt')    # Dependencies needed for your package
)
