#!/usr/bin/env python
import setuptools


if __name__ == '__main__':
    setuptools.setup(
        author='A Composer',
        author_email='composer@email.com',
        install_requires = (
            'abjad',
            ),
        name='trio_score',
        packages=(
            'trio_score',
            ),
        url='https://github.com/composer/trio_score',
        version='0.1',
        zip_safe=False,
        )
