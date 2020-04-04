import paramiko

hostname = "10.199.18.115"
username = "ubuntu"
password = "ubuntu"

commands = [
    "echo ubuntu | sudo -S vgchange -a y",

"echo ubuntu | sudo -S zerofree -v /dev/sdb1",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-root",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-home",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-var+log",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-var+log+audit",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-tmp",

"echo ubuntu | sudo -S zerofree -v /dev/mapper/vg-var",

"echo ubuntu | sudo -S dd if=/dev/zero of=/dev/mapper/vg-swap_1 bs=1M",

"echo ubuntu | sudo -S mkswap /dev/mapper/vg-swap_1"
]

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)


vmkfstools --punchzero /vmfs/volumes/Datastore-$name3/$extract

