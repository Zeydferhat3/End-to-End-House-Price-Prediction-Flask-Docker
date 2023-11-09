from setuptools import setup, find_packages

def get_requirements(file_path):
    with open(file_path, 'r') as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]
        return [req for req in requirements if req != '-e .']

setup(
    name='mlproject',
    version='0.0.1',
    author='Zeyd',
    author_email='zeydferhatz@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
