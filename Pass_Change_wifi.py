
# BABAK
import paramiko
import time

def disable_paging(remote_conn, command="terminal length 0\n", delay=1):
    '''
    Disable the paging of output (i.e. --More--)
    '''
    remote_conn.send("\n")
    remote_conn.send(command)

    # Wait for the command to complete
    time.sleep(delay)

    output = remote_conn.recv(65535)

    return output


def establish_connection(ip, username='', password=''):
    '''
    Use Paramiko to establish an SSH channel to the device
    Must return both return_conn_pre and return_conn so that the SSH
    connection is not garbage collected
    '''

    remote_conn_pre = paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())

    remote_conn_pre.connect(ip, username=username, password=password,
                            look_for_keys=False, allow_agent=False)

    remote_conn = remote_conn_pre.invoke_shell()

    # Clear banner and prompt
    output = remote_conn.recv(65535)

    return (remote_conn_pre, remote_conn, output)


def read_ssh_data(remote_conn, delay=1):
    '''
    Read the data from the ssh channel
    Uses a delay based mechansim
    '''

    # Wait for the command to complete
    time.sleep(delay)
    return remote_conn.recv(65535)



##Color
#!/usr/bin/env python
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)



def main():
    '''
    '''
    Pass = raw_input("ASK for PASS:")
    ip = 'IP Address'

    username = base64.b64decode("Encrypted Username with Hash.py")
    password = base64.b64decode("Encrypted Password with Hash.py")

    (remote_conn_pre, remote_conn, output) = establish_connection(ip, username, password)
    output = disable_paging(remote_conn)
    
    remote_conn.send("\n")
    remote_conn.send("configure terminal\n")
    remote_conn.send("dot11 ssid BT_GUEST\n")
    remote_conn.send("wpa-psk ascii 7 " + Pass + "\n")
    remote_conn.send("exit\n")
    remote_conn.send("exit\n")
    remote_conn.send("write\n")


    output = read_ssh_data(remote_conn)
    print output
    printout("Password Changed Successfuly", RED) 
    print("Password Changed Successfuly")

    remote_conn_pre.close()


def main2():
    '''
    '''
    Pass = raw_input("ASK for PASS:")
    ip = 'IP Address'

    username = base64.b64decode("Encrypted Username with Hash.py")
    password = base64.b64decode("Encrypted Password with Hash.py")

    (remote_conn_pre, remote_conn, output) = establish_connection(ip, username, password)
    output = disable_paging(remote_conn)
    
    remote_conn.send("\n")
    remote_conn.send("configure terminal\n")
    remote_conn.send("dot11 ssid BT_GUEST\n")
    remote_conn.send("wpa-psk ascii 7 " + Pass + "\n")
    remote_conn.send("exit\n")
    remote_conn.send("exit\n")
    remote_conn.send("write\n")


    output = read_ssh_data(remote_conn)
    print output
    printout("Password Changed Successfuly", RED) 
    print("Password Changed Successfuly")

    remote_conn_pre.close()
	
main()
main2()


