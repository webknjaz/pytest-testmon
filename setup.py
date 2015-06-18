from setuptools import setup

setup(
    name='testmon',
    description='testmon has been renamed to pytest-testmon',
    version='0.4.12',
    license='MIT',
    platforms=['linux', 'osx', 'win32'],
    packages=['testmon_renamed'],
    scripts=['testmon_renamed/tmon.py'],
    url='https://github.com/tarpas/testmon/',
    author_email='tibor.arpas@infinit.sk',
    author='Tibor Arpas, Jozef Knaperek, Martin Riesz',
    data_files=([('', ['README.rst']), ]),
    entry_points={
        'pytest11': [
            'old_testmon = testmon_renamed.pytest_testmon',
        ]
    },
    install_requires=['pytest>=2.7.0,<2.9', 'watchdog>=0.8',
                      'coverage>=3.7.1,<4.0', 'coverage_pth'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Programming Language :: Python', ],
)
