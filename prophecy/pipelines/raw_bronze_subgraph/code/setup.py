from setuptools import setup, find_packages
setup(
    name = 'raw_bronze_dynamic',
    version = '1.0',
    packages = find_packages(include = ('raw_bronze_subgraph*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
's3fs', 'prophecy-libs==1.9.9'],
    entry_points = {
'console_scripts' : [
'main = raw_bronze_subgraph.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
