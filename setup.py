import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Something wrong: {e}")
        return False
    return True


if __name__ == "__main__":
    if install_dependencies():
        print("Successed.")
    else:
        print("Not successed")