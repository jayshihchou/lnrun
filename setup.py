import runpy

from setuptools import setup

__version__ = runpy.run_path('lnrun/__version__.py')['__version__']

setup(
    name='lnrun',
    version=__version__,
    author='Chou, Shih-Chieh',
    author_email='jayshihchou@gmail.com',
    url='https://github.com/jayshihchou/lnrun',
    description='Notify via LineNotify after running system commands.',
    packages=['lnrun'],
    license='MIT',
    python_requires='>=3.6',
    keywords=['line', 'notify', 'linenotify', 'lnrun'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS'
    ],
    entry_points={
        'console_scripts': [
            'lnrun=lnrun.__main__:run'
        ]
    }
)
