# audit.py

import subprocess

def run_audit():
    print("Running contract audit...")
    result = subprocess.run(["npx", "hardhat", "verify", "--network", "rinkeby"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_audit()
