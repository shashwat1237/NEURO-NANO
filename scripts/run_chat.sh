#!/bin/bash
# Launches NEURO-NANO in Interactive Conversation Mode

# 1. Navigate to project root (one level up from scripts)
cd "$(dirname "$0")/.."

# 2. Permission Fix (Self-Healing)
if [ ! -x "./tools/llama-cli" ]; then
    echo "Fixing permissions for llama-cli..."
    chmod +x ./tools/llama-cli
fi

# 3. Load System Prompt
SYSTEM_PROMPT=$(cat SYSTEM_PROMPT.txt)

# 4. Launch
# -m: Model path
# -n -1: Infinite generation
# --color: Visuals
# -cnv: Conversation mode
./tools/llama-cli -m models/nano.gguf -n -1 --color -cnv -p "$SYSTEM_PROMPT"