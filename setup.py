from typing import List
from setuptools import find_packages,setup

hypen_e='-e .'
def get_required(file_path:str)->List[str]:
    '''
    return list of requirement

    '''
    required=[]
    with open(file_path) as file_obj:
        required=file_obj.readlines()
        required=[req.replace("\n","")for req in required]

        if hypen_e in required:
            required.remove(hypen_e)
    return required



setup(
name='mlproject',
version='0.0.1',
author='rohit',
author_email='rohitshrivastava0601@gmail.com',
packages=find_packages(),
install_requires=get_required('requirements.txt')
)


