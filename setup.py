from setuptools import setup

setup(
    name="organize-files",
    version="1.0.0",
    description="Organize files by extension into folders with logging and colors",
    author="Muhia",
    packages=["organize_files"],
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "organize-files=organize_files.__main__:main"
        ]
    },
    python_requires=">=3.6"
)
