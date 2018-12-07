#!/usr/bin/env python

from setuptools import setup, find_packages

VERSION = '0.1.0'

ENTRY_POINTS = {
    'orange3.addon': (
        'lookalike = orangecontrib.lookalike',
    ),
    # Entry point used to specify packages containing widgets.
    'orange.widgets': (
        # Syntax: category name = path.to.package.containing.widgets
        # Widget category specification can be seen in
        #    orangecontrib/datafusion/widgets/__init__.py
        'Lookalike = orangecontrib.lookalike.widgets',
    ),
    # Register widget help
    "orange.canvas.help": (
    'html-index = orangecontrib.lookalike.widgets:WIDGET_HELP_PATH',
    ),
}

if __name__ == '__main__':
    setup(
        name="Orange3-Lookalike-Demo",
        description="Orange add-on for demonstration purposes.",
        version=VERSION,
        author='Bioinformatics Laboratory, FRI UL',
        author_email='contact@orange.biolab.si',
        url='https://github.com/biolab/lookalike-demo',
        keywords=(
            'orange3 add-on',
        ),
        packages=find_packages(),
        package_data={
            "orangecontrib.lookalike.widgets": ["icons/*.svg","data/*.xml"],
        },
        install_requires=[
            'Orange3',
            'numpy',
            'scipy',
            'scikit-learn',
            'pyqtgraph',
            'AnyQt>=0.0.8',
            'serverfiles',
            # For Webcam widget
            'opencv-python'
        ],
        extras_require={
            ':python_version<"3.5"': [
                "typing"
            ]
        },
        entry_points=ENTRY_POINTS,
        namespace_packages=['orangecontrib'],
        include_package_data=True,
        zip_safe=False,
    )
