from setuptools import find_packages, setup
from typing import List


def get_requirements()->List[str]:
    requiremnt_lst:List[str]=[]
    try:
        
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requiremnt= line.strip()
                if requiremnt and requiremnt!='-e .':
                    requiremnt_lst.append(requiremnt)

    except FileNotFoundError:
        print("requirement.txt file is not found")

    return requiremnt_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Venkatesh salla",
    author_email="venkatesh.salla01@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)