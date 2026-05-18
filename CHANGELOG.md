# Changelog

All notable changes to this repository are recorded here.

## [0.4.0] - 2026-05-18

### Changed

- Moved the installable skill from `skills/project-progress-memory-logger/` to the repository root.
- Moved script tests to the root `tests/` directory.
- Updated root README files to show the root-level skill layout.
- Updated `.gitignore` to exclude the local `Docs/` progress memory tree.

### Removed

- Removed the obsolete nested skill README and nested `skills/` directory layout.
- Removed generated `__pycache__` directories from the working tree.

## [0.3.0] - 2026-05-14

### Changed

- Returned the repository to a single-skill layout for `project-progress-memory-logger`.
- Rewrote root `README.md` and `README.zh-CN.md` for a single skill with concise English/Chinese documentation links.
- Updated maintenance docs, install guide, and release checklist for the one-skill-per-repository model.
- Updated repository validation to reject extra installable skill directories.

### Removed

- Removed `project-progress-memory-logger-ch` from this repository. A Chinese workflow skill should be maintained as its own repository if needed.

## [0.2.0] - 2026-05-13

### Added

- Added `project-progress-memory-logger-ch`, a Chinese workflow version of Project Progress Memory Logger.
- Added repository-level documentation under `docs/`.
- Added repository-level batch test runner at `tests/run_all_skill_tests.py`.

### Changed

- Converted the repository from a single-skill project into a multi-skill collection.
- Moved the English skill into `skills/project-progress-memory-logger/`.
- Kept each skill self-contained so users can install one skill without repository-level `shared/` files.

## [0.1.0] - 2026-05-13

### Added

- Initial `project-progress-memory-logger` skill.
- Added templates, references, scripts, examples, tests, MIT license, and README.
