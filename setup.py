from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='hw7 Clean_folder',
    # url='http://github.com/dummy_user/useful',
    author='Nissa Boitsun',
    author_email='dgofreyod@gmail.com',
    license='Nissa',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    # install_requires=['markdown'],
    entry_points={'console_scripts': [
        'clean_folder=clean_folder.main:start']}
)