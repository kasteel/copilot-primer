#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir/../../python-app"

if ! uv run ruff check app tests scripts; then
  exit 2
fi