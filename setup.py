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
    url = 'https://github.com/ghurone/jupiterweb_scraper',
    project_urls = {
        'Código fonte': 'https://github.com/ghurone/jupiterweb_scraper',
    },
    install_requires=['beautifulsoup4>=4.11.1', 'lxml>=4.9.1', 'requests>=2.28.1'],
    license = 'MIT',
    keywords = 'jupiterweb disciplinas usp ghuron',
    python_requires='>=3.8',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent'
    ]
)