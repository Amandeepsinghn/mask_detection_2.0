from setuptools import setup,find_packages


with open("README.md","r",encoding='utf-8') as f:
    discription_=f.read()


setup(
    name="mask_detection",
    author="Code_master",
    version="1.0",
    author_email="amandeepsingh.kiallay@gmail.com",
    url=f"https://github.com/Amandeepsinghn/mask_detection_2.0",
    packages=find_packages(where="src"),
    description="app to detect mask",
    long_description=discription_,
    package_dir={"":"src"}
)