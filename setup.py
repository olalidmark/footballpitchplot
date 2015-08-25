from setuptools import setup

setup(
    name='footballpitchplot',
    version='0.1',
    packages=['pitchplotter'],
    url='https://github.com/olalidmark/footballpitchplot',
    license='MIT',
    author='fantomen',
    author_email='olalidmark@gmail.com',
    description='Python library using Plotly for plotting a football pitch with events.',
    keywords=['football', 'soccer', 'metrics', 'sports', 'statistics', 'plotly', 'plot'],  # arbitrary keywords
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',

    ],
    install_requires=['plotly'],
)
