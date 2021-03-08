from distutils.core import setup
from distutils.command.install import install
from subprocess import call
class Install(install):
    def run(self):
        install.run(self)
        for line in open('requirements.txt').readlines():
            if len(line) > 1: call(['pip', 'install', line.replace('\n', '')])
setup(
    name = 'PyDonno',
    version = '1.0.0',
    description = 'All my packages',
    long_description = open('README.txt').read(),
    url = 'https://github.com/donno2048/PyDonno',
    license = 'MIT',
    author = 'Elisha Hollander',
    author_email = 'just4now666666@gmail.com',
    cmdclass = {'install': Install}
)