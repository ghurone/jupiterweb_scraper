from email.encoders import encode_noop
from setuptools import setup
import jupiterweb as jup

long_description = open('README.md', encoding='utf8').read()

setup(
    name = 'jupiterweb',
    version = jup.__version__,
    author = jup.__author__,
    author_email = 'ghuron@usp.br',
    packages = ['jupiterweb'],
    description = 'Um scraper de disciplinas do jupiterweb',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/ghurone/jupiterweb-scraper',
    project_urls = {
        'Código fonte': 'https://github.com/ghurone/jupiterweb-scraper',
    },
    install_requires=['beautifulsoup4>=4.10.0', 'lxml>=4.6.3', 'requests>=2.26.0'],
    license = 'MIT',
    keywords = 'jupiterweb ghuron disciplinas usp',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent'
    ]
)