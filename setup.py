from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/mypackage',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
    