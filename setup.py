from setuptools import setup, find_packages

setup(
    name='openmacro',
    version='0.0.4',
    packages=find_packages(include=['openmacro', 'openmacro.core', 'openmacro.cli', 'openmacro.core.utils']),
    install_requires=["gradio_client", "toml", "rich"],
    entry_points={
        'console_scripts': [
            'macro=openmacro.__main__:main',  
        ],
    },
    include_package_data=True, 
    package_data={
        'openmacro': ['core/config.default.toml', 'core/prompts/*', 'extensions/*'],  
    },
    author='Amor Budiyanto',
    author_email='amor.budiyanto@gmail.com',
    description='Autonomous LLM personal agent.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amooo-ooo/openmacro',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
