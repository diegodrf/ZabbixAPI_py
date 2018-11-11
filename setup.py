from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ZabbixAPI_py',
    version='1.0.0',
    author='Diego Rodrigues',
    author_email='diego.rdfaria@gmail.com',
    packages=['ZabbixAPI_py'],
    install_requires=[
        'requests',
        'colorama'
    ],
    description='Biblioteca para contectar na API do Zabbix',
    long_description=long_description,
    url='https://github.com/diegodrf/ZabbixAPI_py',
    project_urls={
        'Código-fonte': 'https://github.com/diegodrf/ZabbixAPI_py',
        'Download': 'https://github.com/diegodrf/ZabbixAPI_py/archive/master.zip'
    },
    license='MIT',
    keywords=['zabbix', 'api'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Monitoring'
    ]
)
