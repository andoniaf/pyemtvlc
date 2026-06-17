# AGENTS.md

Context for AI assistants and contributors working on this repository.

## What this project does

`pyemtvlc` is a Python CLI tool and library for querying real-time EMT Valencia bus arrival
times. Given a bus stop number (and optionally a line number), it prints the next arrivals.

## Data source

Endpoint: `https://geoportal.emtvalencia.es/EMT/mapfunctions/MapUtilsPetitions.php?sec=getSAE`

- Accepts POST requests with parameters `parada` (stop number) and optionally `linea` (line number).
- Returns XML.
- **Unofficial, undocumented endpoint** — it can change without notice.

## Repository layout

```
pyemtvlc          # CLI entrypoint (executable script)
utils/
  emtinfo.py      # HTTP POST request to the EMT endpoint
  parser.py       # XML parsing and message formatting
test/             # unittest-based tests, using the `responses` library to mock HTTP
setup.py          # package metadata
tox.ini           # tox environments: py311/py312/py313 + linters (flake8, pylint, bandit)
```

## Running tests

```bash
pytest test/
# or
tox
```

## Conventions

- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/).
- Do not add AI co-author attribution to commits or PRs.

## Releasing

Releases are published to PyPI automatically via the `.github/workflows/publish.yml` workflow
when a GitHub Release is published, using PyPI Trusted Publishing (OIDC — no stored secrets).

Before the first release, configure the Trusted Publisher on PyPI:
- Project → Publishing → Add publisher
- Repository: `andoniaf/pyemtvlc`, workflow: `publish.yml`
