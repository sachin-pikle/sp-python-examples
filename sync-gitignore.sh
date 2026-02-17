#!/usr/bin/env bash
set -euo pipefail

# Sync a template .gitignore to immediate subdirectories of a root path.
# Default behavior: create .gitignore if missing; do not overwrite existing ones.
#
# Usage:
#   sync-gitignore.sh [--root PATH] [--template PATH] [--overwrite]
#
# Examples:
#   sync-gitignore.sh                             # use defaults
#   sync-gitignore.sh --root /path/to/projects    # custom root
#   sync-gitignore.sh --template /path/tmpl       # custom template
#   OVERWRITE=true sync-gitignore.sh              # env var to force overwrite
#   sync-gitignore.sh --overwrite                 # flag to force overwrite

ROOT_DEFAULT="/Users/$(whoami)/Code/python/sp-python-examples"
TEMPLATE_DEFAULT="/Users/$(whoami)/Code/python/sp-python-examples/atbs-12-regex/.gitignore"

ROOT="$ROOT_DEFAULT"
TEMPLATE="$TEMPLATE_DEFAULT"
OVERWRITE="${OVERWRITE:-false}"

print_help() {
  grep '^#' "$0" | sed -e 's/^# \{0,1\}//'
}

# Basic arg parsing for long options
while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT="${2:-}"
      shift 2
      ;;
    --template)
      TEMPLATE="${2:-}"
      shift 2
      ;;
    --overwrite)
      OVERWRITE="true"
      shift 1
      ;;
    -h|--help)
      print_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      print_help
      exit 1
      ;;
  esac
done

if [[ ! -d "$ROOT" ]]; then
  echo "Root directory not found: $ROOT" >&2
  exit 2
fi
if [[ ! -r "$TEMPLATE" ]]; then
  echo "Template .gitignore not found or unreadable: $TEMPLATE" >&2
  exit 3
fi

created=0
updated=0
skipped=0

for d in "$ROOT"/*; do
  [[ -d "$d" ]] || continue
  target="$d/.gitignore"
  if [[ -f "$target" ]]; then
    if [[ "$OVERWRITE" == "true" ]]; then
      cp -f "$TEMPLATE" "$target"
      echo "updated: $target"
      ((updated++))
    else
      echo "skip (exists): $target"
      ((skipped++))
    fi
  else
    cp "$TEMPLATE" "$target"
    echo "created: $target"
    ((created++))
  fi
done

echo "Summary: created=$created updated=$updated skipped=$skipped (root=$ROOT)"
