from setuptools import setup, find_packages


VERSION = "0.0.1"
DESCRIPTION = "All in one logger"
LONG_DESCRIPTION = "Package for manage all logs you need"

setup(
    name="monkey_logger",
    version=VERSION,
    author="Hernán Varillas",
    author_email="<hernan.varillas93@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_required=[],
    keywords=["python", "test", "log"],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
