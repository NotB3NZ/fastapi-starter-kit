# Contributing to FastAPI Starter Kit

Thank you for considering contributing to the FastAPI Starter Kit! We welcome all contributions — bug fixes, new features, documentation improvements, and more.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Quality](#code-quality)
- [Commit Message Convention](#commit-message-convention)
- [Pull Request Process](#pull-request-process)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive experience for everyone.

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:

   ```bash
   git clone https://github.com/<your-username>/fastapi-starter-kit.git
   cd fastapi-starter-kit
   ```

3. **Add the upstream remote**:

   ```bash
   git remote add upstream https://github.com/shopnilsazal/fastapi-starter-kit.git
   ```

4. **Create a feature branch** from `main`:

   ```bash
   git checkout -b feat/my-new-feature
   ```

## Development Setup

### Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/) (v2+)

### Install Dependencies

```bash
uv sync
```

### Start the Services

```bash
docker compose up --build
```

This brings up the FastAPI backend, PostgreSQL, and Redis. See the [README](README.md) for full details.

### Run Without Docker

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8008
```

> [!NOTE]
> You'll need a running PostgreSQL and Redis instance. Update `DB_HOST` in `.env` to `localhost` when running outside Docker.

## Code Quality

This project uses **pre-commit** hooks to enforce code quality automatically.

### Setup Hooks

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

### Linting & Formatting

We use [Ruff](https://docs.astral.sh/ruff/) for both linting and formatting:

```bash
# Run all hooks against every file
pre-commit run --all-files

# Or run ruff standalone
ruff check . --fix
ruff format .
```

> [!IMPORTANT]
> All code must pass linting and formatting checks before it can be merged.

## Commit Message Convention

This project enforces **[Conventional Commits](https://www.conventionalcommits.org/)** via [gitlint](https://jorisroovers.com/gitlint/).

### Format

```
<type>: <description>

[optional body]

[optional footer(s)]
```

### Allowed Types

`story` · `epic` · `fix` · `feat` · `chore` · `docs` · `style` · `refactor` · `perf` · `test` · `revert` · `ci` · `build`

### Rules

- Title must be **5–90 characters**
- Do **not** include `WIP` in the title
- Merge, revert, fixup, and squash commits are automatically ignored

### Examples

```
feat: add user authentication endpoint
fix: resolve database connection timeout
docs: update API usage examples
chore: upgrade ruff to v0.7.0
```

## Pull Request Process

1. **Sync with upstream** before starting work:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Make your changes** in a focused, single-purpose branch.
3. **Ensure all checks pass**:

   ```bash
   pre-commit run --all-files
   ```

4. **Push your branch** and open a Pull Request against `main`.
5. **In your PR description**, include:
   - A clear summary of what changed and why
   - Any related issue numbers (e.g., `Closes #42`)
   - Screenshots or logs if applicable

6. **Address review feedback** promptly. Push additional commits — we can squash on merge.

> [!TIP]
> Keep PRs small and focused. Smaller PRs are easier to review and merge faster.

## Reporting Issues

When opening an issue, please include:

- **A clear title** describing the problem or feature request
- **Steps to reproduce** (for bugs)
- **Expected vs. actual behavior**
- **Environment details** — OS, Python version, Docker version
- **Logs or screenshots** if applicable

---

Thank you for helping improve FastAPI Starter Kit!
