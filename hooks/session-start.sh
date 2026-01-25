#!/bin/bash
# DRIVER Session Start Hook
# Injects the using-driver skill at the start of every session

SKILL_PATH="${CLAUDE_PLUGIN_ROOT}/skills/using-driver/SKILL.md"

if [ -f "$SKILL_PATH" ]; then
    echo "<EXTREMELY-IMPORTANT>"
    cat "$SKILL_PATH"
    echo "</EXTREMELY-IMPORTANT>"
fi
