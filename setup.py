from setuptools import setup, find_packages

requirements = [
    'aiohttp',
]

setup(
    name='azura-cast-api-client',
    packages=find_packages(include=['azura_cast_api_client']),
    python_requires='>=3.7',
    version='0.0.1',
    description='API client for AzuraCast server',
    author='https://github.com/chloemby',
    license='MIT',
)
