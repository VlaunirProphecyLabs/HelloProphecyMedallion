from setuptools import setup, find_packages
setup(
    name = 'silver_customers',
    version = '1.0',
    packages = find_packages(include = ('silver_customers*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
's3fs', 'prophecy-libs==1.9.29'],
    entry_points = {
'console_scripts' : [
'main = silver_customers.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
