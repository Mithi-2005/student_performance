from setuptools import find_packages,setup
HYPEN_E_DOT='-e .'
def get_req(file_path):
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',' ') for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
    name='Student Performance',
    version='1.0',
    author='Mithilesh',
    author_email='kvmithilesh10@gmail.com',
    packages=find_packages(), ### Will check the folders where __init__.py is there and take it as package
    install_requires=get_req('requirements.txt')
)