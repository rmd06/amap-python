from setuptools import setup, find_namespace_packages

requirements = [
    "nibabel",
    "numpy",
    "configparser",
    "pandas",
    "scikit-image",
    "tqdm",
    "natsort",
    "multiprocessing-logging",
    "configobj",
    "slurmio",
    "brainio>=0.0.9",
    "fancylog",
    "micrometa",
    "napari>=0.2.8",
    "scikit-image",
    "luddite",
]


setup(
    name="amap",
    version="0.1.2",
    description="Automated mouse atlas propagation",
    install_requires=requirements,
    extras_require={
        "dev": [
            "sphinx",
            "recommonmark",
            "sphinx_rtd_theme",
            "pydoc-markdown",
            "black",
            "pytest-cov",
            "pytest",
            "gitpython",
            "coveralls",
            "coverage<=4.5.4",
        ]
    },
    python_requires=">=3.6",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "amap = amap.cli:main",
            "amap_gui = amap.cli:gui",
            "amap_download = amap.download.cli:main",
            "amap_vis = amap.vis.vis:main",
        ]
    },
    url="https://github.com/SainsburyWellcomeCentre/amap-python",
    author="Adam Tyson, Charly Rousseau, Christian Niedworok",
    author_email="adam.tyson@ucl.ac.uk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
