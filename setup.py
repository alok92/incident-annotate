from setuptools import setup, find_packages

setup(
    name="incident_annotator",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'incident-annotator=incident_annotator.main:main'
        ]
    },
    author="Alok",
    description="A CLI tool to annotate incidents in Grafana or Markdown.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.7',
)
