from setuptools import setup

setup(
    name='Youtube MP3 Downloader',
    version='1.0',
    author='Özer Özdaş',
    author_email='ozer@ozdas.org',
    description='A simple Youtube MP3 downloader.',
    packages=[],
    install_requires=[
        'pytube',
        'tkinter',
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