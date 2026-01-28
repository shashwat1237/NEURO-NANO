import subprocess
import sys
import platform
import os
import stat

# INTEGRATION CONFIGURATION
# Detect OS to choose correct binary extension
if platform.system() == "Windows":
    EXT = ".exe"
else:
    EXT = ""

# Dynamic paths to prevent "Path Hell"
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
PROJECT_ROOT = os.path.dirname(BASE_DIR)              
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "nano.gguf")

# AUDIT FIX: Fallback logic for legacy binaries (main vs llama-cli)
POSSIBLE_BINARIES = ["llama-cli", "main", "server"]
CLI_PATH = None

for binary_name in POSSIBLE_BINARIES:
    path_check = os.path.join(PROJECT_ROOT, "tools", binary_name + EXT)
    if os.path.exists(path_check):
        CLI_PATH = path_check
        break

def ensure_permissions(path):
    """Auto-heals 'Permission Denied' on Linux/Mac"""
    if platform.system() != "Windows":
        try:
            st = os.stat(path)
            os.chmod(path, st.st_mode | stat.S_IEXEC)
        except Exception:
            pass 

def execute_nano(prompt):
    if CLI_PATH is None:
        return f"CRITICAL: No valid engine found in 'tools'. Checked: {POSSIBLE_BINARIES}"
    
    if not os.path.exists(MODEL_PATH):
        return f"CRITICAL: Model not found at {MODEL_PATH}. Check 'models' folder."

    ensure_permissions(CLI_PATH)

    command = [
        CLI_PATH,
        "-m", MODEL_PATH,
        "-p", prompt,
        "--no-display-prompt", 
        "-n", "1024" # Output limit
    ]
    
    try:
        # encoding='utf-8' is vital for Windows emoji/symbol compatibility
        result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8')
        return result.stdout
    except Exception as e:
        return f"Execution Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        user_input = input("ENTER TASK: ")
        
    print(f"\n> NEURO-NANO PROCESSING: {user_input}...\n")
    # Enforce logic-only persona via Prompt Injection
    system_wrapper = f"You are NEURO-NANO. {user_input} Provide code/text only. Do not explain."
    
    response = execute_nano(system_wrapper)
    print(response)