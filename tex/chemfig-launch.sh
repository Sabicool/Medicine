#!/usr/bin/env zsh
# chemfig-launch.sh — invoke medicine/new-chemfig via emacsclient
# Used by the Obsidian Templater script; handles the custom socket path
# that Doom sets via (setq server-socket-dir ...).
set -euo pipefail

name="${1:?Usage: chemfig-launch.sh <diagram-name>}"
socket="${HOME}/.config/emacs/.local/cache/server/server"

if [[ -S "$socket" ]]; then
  emacsclient -n --socket-name="$socket" -e "(medicine/new-chemfig \"${name}\")"
else
  # Fall back to default socket discovery
  emacsclient -n -e "(medicine/new-chemfig \"${name}\")"
fi
