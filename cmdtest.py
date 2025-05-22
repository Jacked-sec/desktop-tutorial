import subprocess

def run_whoami():
    try:
        result = subprocess.run(["tasklist"], capture_output=True, text=True, shell=True)
        print("Username:", result.stdout.strip())
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    run_whoami()