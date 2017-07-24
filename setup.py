from setuptools import setup

requires = ['nfcpy']

setup(
    name='nfcpy_id_reader',
    version='0.0.3',
    description='Read the ID of an NFC Tag with nfcpy',
    url='https://github.com/mascii/nfcpy_id_reader',
    author='Masaki Koyanagi',
    author_email='mascii@gmail',
    license='EUPL 1.1',
    keywords='nfc pasori',
    packages=['nfcpy_id_reader'],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ],
)

