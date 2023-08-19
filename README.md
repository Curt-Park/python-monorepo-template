# Python Mmonorepo Template

Python Monorepo Temlate with [Pants](https://www.pantsbuild.org/).

## Items
- [x] Small python projects with dependency
- [x] Project execution
- [x] Formatting (black, isort)
- [x] Linting (flake8, pylint, pydocstyle)
- [x] Unit Test
- [ ] Docker build
- [ ] GitHub actions

## Project Structure
```bash
.
└── libs
    ├── base   # base has add2(int, int)
    └── fancy  # fancy has add3(int, int, int) method which calls add2
```

## Prerequisites

- For Linux
```bash
curl --proto '=https' --tlsv1.2 -fsSL https://static.pantsbuild.org/setup/get-pants.sh | bash
```

- For Mac
```bash
brew install pantsbuild/tap/pants
```

## How to run
```bash
# How to execute
pants run libs/base/main.py
pants run libs/fancy/main.py

# How to format
pants fmt ::             # for all projects
pants fmt libs/base::    # for base
pants fmt libs/fancy::   # for fancy

# How to lint
pants lint ::            # for all projects
pants lint libs/base::   # for base
pants lint libs/fancy::  # for fancy

# How to run unit tests
pants test ::            # for all projects
pants test libs/base::   # for base
pants test libs/fancy::  # for fancy
```

## References
- https://github.com/pantsbuild/example-python
- https://github.com/tweag/python-monorepo-example
