import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', "r") as fh:
    required = fh.read().splitlines()
    print(required)


setuptools.setup(
    name="svm_eshelukhina",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eshelukhina/HSE2022-EngineeringPracticesInML",
    packages=setuptools.find_packages(),
    install_requires=required,
    # Требуемая версия Python.
    python_requires='>=3.8',
)
