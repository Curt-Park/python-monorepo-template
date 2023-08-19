# Python Mmonorepo Template

Python Monorepo Temlate with [Pants](https://www.pantsbuild.org/).

## Items
- [ ] Small python projects with dependency
- [ ] Project setup
- [ ] Project execution
- [ ] Formatting (black, isort)
- [ ] Linting (flake8, pylint, pyright)
- [ ] Unit Test
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
TBD

## References
- https://github.com/pantsbuild/example-python
- https://github.com/tweag/python-monorepo-example
