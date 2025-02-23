from skbuild import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name="fenics-basix",
      python_requires='>=3.7.0',
      version="0.7.0.dev0",
      description='Basix Python interface',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/FEniCS/basix",
      author='FEniCS Project',
      author_email="fenics-dev@googlegroups.com",
      maintainer_email="fenics-dev@googlegroups.com",
      license="MIT",
      packages=["basix"],
      package_data={"basix": ["py.typed"]},
      install_requires=["numpy>=1.21"],
      extras_require={
          "docs": ["markdown", "pylit3", "pyyaml", "sphinx==5.0.2", "sphinx_rtd_theme"],
          "lint": ["flake8", "pydocstyle"],
          "optional": ["numba", "fenics-ufl@git+https://github.com/fenics/ufl"],
          "test": ["pytest", "sympy", "scipy", "matplotlib", "fenics-basix[optional]"],
          "ci": ["mypy", "pytest-xdist", "fenics-basix[docs]", "fenics-basix[lint]", "fenics-basix[optional]",
                 "fenics-basix[test]"]
      },
      package_dir={"": "python"},
      cmake_install_dir="python/basix/")
