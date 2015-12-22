import os
from setuptools import setup, find_packages

execfile(os.path.join(os.path.pardir, 'common_setup.py'))

classifiers = [
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Testing',
    'Topic :: Utilities',
    'Intended Audience :: Developers',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
]

install_requires = ['six',
                    'pytest']

tests_require = ['pytest-cov',
                 ]

entry_points = {
    'pytest11': [
        'listener = pytest_listener',
    ]
}

if __name__ == '__main__':
    kwargs = common_setup('pytest_listener')
    kwargs.update(dict(
        name='pytest-listener',
        description='A simple network listener',
        author='Tim Couper',
        author_email='drtimcouper@gmail.com',
        classifiers=classifiers,
        install_requires=install_requires,
        tests_require=tests_require,
        packages=find_packages(exclude='tests'),
        entry_points=entry_points,
    ))
    setup(**kwargs)
