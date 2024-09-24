from setuptools import setup, find_packages

setup(
    name='de',  # Replace with your package name
    version='0.1.0',   # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        # List your package dependencies here
    ],
    author="DevaDharshini-ihub",
    author_email='deva.d.ihub@snsgroups.com',  # Your email
    description=' a greeting messages deva.',
    long_description=open('README.md').read(),  # Use README.md for long description
    long_description_content_type='text/markdown',  # Your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
          # Change to your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)