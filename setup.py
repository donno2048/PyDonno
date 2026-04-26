from setuptools import setup
from setuptools.command.install import install
from subprocess import call
from sys import executable
class Install(install):
    def run(self):
        install.run(self)
        for line in open('requirements.txt').readlines():
            if len(line) > 1 and not line.startswith("#"): call([executable, '-m', 'pip', 'install', line.replace('\n', '')])
setup(
    name = 'PyDonno',
    version = '1.3.1',
    description = 'All my packages',
    long_description = open('README.md').read().replace('`', '').replace('sh', '').replace('\n', '\n\n'),
    long_description_content_type="text/markdown",
    url = 'https://github.com/donno2048/PyDonno',
    license = 'MIT',
    author = 'Elisha Hollander',
    author_email = 'just4now666666@gmail.com',
    include_package_data=True,
    cmdclass = {'install': Install}
)
