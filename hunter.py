import subprocess

class bcolors: # Colours for debug
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[31m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    # Command to run in the child process
    command = ['strace', 'nc', '-lvnp', '4444']

    # Create the subprocess and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Analyze syscall
    for line in process.stderr:
        
        # Begin triage
        if "system(/bin/bash)" in line: 
            print(bcolors.ERROR + "[ANOMALY DETECTED]" + bcolors.ENDC, line.strip())
        elif "/bin/bash" in line: 
            print(bcolors.WARNING + "[POTENTIAL ANOMALY]" + bcolors.ENDC, line.strip())
        else:
            print(bcolors.OKGREEN + "[SYSCALL]" + bcolors.ENDC, line.strip())

    # Wait for the child process to finish
    process.wait()

    # Print the child process return code
    print("Child process exited with code:", process.returncode)

if __name__ == '__main__':
    main()