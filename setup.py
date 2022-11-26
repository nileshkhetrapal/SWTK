from setuptools import setup, find_packages

setup(
    name='SWTK',
    version='0.1',
    description='An experimental Unsupervised Learning Log Anomaly Detection toolkit. YOU ARE BEAUTIFUL!',
    url='https://github.com/nileshkhetrapal/SWTK',
    author='Nilesh Khetrapal',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'SWTK = SWTK:main',
        ],
    },
)

