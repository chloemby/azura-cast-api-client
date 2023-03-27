from setuptools import setup

requirements = [
    'aiohttp',
]

setup(
    name='azura-cast-api-client',
    packages=['azura_cast_api_client'],
    python_requires='>=3.7',
    requirements=requirements,
    version='0.0.1',
    description='API client for AzuraCast server',
    author='https://github.com/chloemby',
    license='MIT',
)
