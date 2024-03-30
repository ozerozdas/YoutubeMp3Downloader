"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'packages': [],
    'iconfile': 'icon.png',
    'plist': {
        'CFBundleName': 'Youtube Mp3 Downloader',
        'CFBundleDisplayName': 'Youtube Mp3 Downloader',
        'CFBundleGetInfoString': 'Youtube Mp3 Downloader',
        'CFBundleIdentifier': 'com.ozerozdas.youtubemp3downloader',
        'CFBundleVersion': '0.1.0',
        'CFBundleShortVersionString': '0.1.0',
        'CFBundleExecutable': 'Youtube Mp3 Downloader',
        'CFBundleIconFile': 'icon.png',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
