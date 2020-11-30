
from distutils.core import setup

setup(
    name='kabuka',
    packages=['kabuka'],
    version='0.1',
    license='MIT',
    description='get latest stock price from Yahoo! Finance',
    author='Danaipat Sodkomkham',
    author_email='sdanaipat@gmail.com',
    url='https://github.com/sdanaipat/kabuka',
    download_url='https://github.com/sdanaipat/kabuka/archive/kabuka-0.1.tar.gz',
    keywords=['stock price', 'yahoo finance', 'market price', 'get latest stock price'],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Financial Data API',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
