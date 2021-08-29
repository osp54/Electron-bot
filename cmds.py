from os import system
while True:
    cmd = input()
    if cmd == 'exit':
        exit(-3)
    if cmd == 'restart':
        system("./start.sh")
