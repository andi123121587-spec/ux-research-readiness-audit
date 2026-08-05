#!/usr/bin/env bash
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_PROMPT="$ROOT/examples/example-prompt.md"

echo "This is a command template for one local regression run."
echo "Run it from a project with Codex installed and authenticated:"
echo
echo '  cd examples/minimal-input'
echo '  CODEX_SQLITE_HOME="/tmp/uxra-codex-sqlite" codex exec --ephemeral --sandbox read-only "$(cat "'"$SKILL_PROMPT"'")"'
echo
echo "Do not commit the output, logs, or SQLite directory."
