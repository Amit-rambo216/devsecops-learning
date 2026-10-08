def hello():
    return "Hello DevSecOps v2"

if __name__ == "__main__":
    print(hello())
    import subprocess


def run_command(user_input):
    return subprocess.run(user_input, shell=True, capture_output=True, text=True)