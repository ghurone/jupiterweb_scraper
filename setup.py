from setuptools import setup

long_description = open('README.md', encoding='utf8').read()

setup(
    name = 'jupiterweb',
    version = '1.0.3',
    author = 'Érick Ghuron',
    author_email = 'ghuron@usp.br',
    packages = ['jupiterweb'],
    description = 'Um scraper de disciplinas do jupiterweb',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/ghurone/jupiterweb-scraper',
    project_urls = {
        'Código fonte': 'https://github.com/ghurone/jupiterweb-scraper',
    },
    license = 'MIT',
    keywords = 'jupiterweb ghuron disciplinas',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent'
    ]
)