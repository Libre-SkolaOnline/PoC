import os
import sys
import subprocess

DIR = "modules"

def install_dependencies():
    dependencies = ["requests"]
    for package in dependencies:
        try:
            __import__(package)
        except ImportError:
            print(f"Instaluji chybějící balíček: {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", package])

def main():
    while True:

        scripts = sorted([f for f in os.listdir(DIR) if f.endswith(".py") and f != "auth.py"])

        print()
        for i, script in enumerate(scripts, 1):
            print(f"{i}) {script}")
        print("0) Exit")

        try:
            choice = int(input("> "))
        except ValueError:
            continue

        if choice == 0:
            break

        if 1 <= choice <= len(scripts):
            subprocess.run([sys.executable, scripts[choice - 1]], cwd=DIR)
            input("\nStiskni Enter...")

if __name__ == "__main__":
    install_dependencies()
    main()