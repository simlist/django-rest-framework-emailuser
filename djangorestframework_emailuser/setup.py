from setuptools import setup

setup = (
    name='djangorestframework_emailuser',
    version='0.1.0dev0',
    author='MS List',
    author_email='simlist@gmail.com',
    packages=['emailuser',],
    url='https://github.com/simlist/djangorestframework_emailuser',
    license='MIT',
    description=(
        'A user for djangorestframework that uses an email as the username.'
    )
    install_requires=[],
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ]
)