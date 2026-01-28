@echo off
:: Launches NEURO-NANO in Interactive Conversation Mode

cd ..
tools\llama-cli.exe -m models\nano.gguf -n -1 --color auto -cnv -f SYSTEM_PROMPT.txt
pause