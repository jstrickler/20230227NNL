from subprocess import run, PIPE
import shlex

cmd = "netstat -n"
cmd_words = shlex.split(cmd)

# just run command
run(cmd_words)

# run and capture output
process = run(cmd_words, stdout=PIPE)
raw_output = process.stdout  # stdout is bytes object
output = raw_output.decode()
output_lines = output.splitlines()
print()
print(f"output_lines: {output_lines}")
print('-' * 60)
established_connections = [line for line in output_lines if "ESTAB" in line]
for connection in established_connections:
    protocol, local, remote, _ = connection.split()
    local_ip, local_port = local.split(':')
    remote_ip, remote_port = remote.split(':')
    print(f"{local_ip:15s} {local_port:>6s} {remote_ip:15s} {remote_port:>6s}")

run("notepad")

# run("c:/windows/bin/hijinks.exe arg arg")
