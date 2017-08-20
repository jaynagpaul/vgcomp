from setuptools import setup

with open('./requirements.txt') as f:
    deps = f.read().split('\n')

setup(
    name="vgcomp",
    version="1.0.0",
    description="Vainglory Comp Generator",
    author="SpiesWithin",
    author_email="hi@jaynagpaul.com",
    url="https://github.com/jaynagpaul/vgcomp",
    packages=["vgcomp"],
    install_requires=deps,
    entry_points={
        'console_scripts': [
            'vgcomp = vgcomp.cli:cli',
        ],
    }
)
