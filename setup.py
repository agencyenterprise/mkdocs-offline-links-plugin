from setuptools import setup, find_packages


setup(
    name='mkdocs-offline-links-plugin',
    version='0.1.0',
    description='A MkDocs plugin to make links to other pages in the site work offline.',
    long_description='',
    keywords='mkdocs',
    url='',
    author='Charles Guan',
    author_email='charles@ae.studio',
    python_requires='>=3.9',
    install_requires=[
        'mkdocs>=1.5.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9'
        'Programming Language :: Python :: 3.10'
        'Programming Language :: Python :: 3.11'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'offline-links = mkdocs_offline_links.plugin:OfflineLinksPlugin'
        ]
    }
)
