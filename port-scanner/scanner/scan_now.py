import socket
import threading
import sqlite3
import os


def portscan(ip, port_for_scan):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con = s.connect((ip, port_for_scan))
        open_ports.append(str(port_for_scan))
        con.close()
    except TimeoutError:
        pass
    except Exception as e:
        pass


def scan_one_host(ip):
    start_port = 1
    for x in range(1, 65535):
        t = threading.Thread(target=portscan, kwargs={'ip': ip, 'port_for_scan': start_port})
        start_port += 1
        t.start()
        if start_port == 65535:
            t.join()


connection = sqlite3.connect('../db.sqlite3')
cursor = connection.cursor()
cursor.execute("SELECT id, name, allow_ports, open_ports FROM scanner_ip")
ips = cursor.fetchall()

for ip in ips:

    open_ports = []
    split_ports = []
    open_and_not_allowed_ports = []
    log_dir_path = os.path.dirname(os.path.realpath(__file__)) + '\logs\\'

    scan_one_host(ip[1])
    allow_ports = ip[2].split(',')

    for port in allow_ports:
        if '-' in port:
            port = port.split('-')
            for i in range(int(port[0]), int(port[1]) + 1):
                split_ports.append(i)
        else:
            split_ports.append(port)

    for p in open_ports:
        if p not in allow_ports:
            open_and_not_allowed_ports.append(p)

    open_ports = open_and_not_allowed_ports
    # open_ports.sort()

    if len(open_ports) > 10:
        with open(f'{log_dir_path}{ip[1]}.log', 'w') as log:
            log.write(','.join(open_ports))

        open_ports = 'больше 10'
        cursor.execute(f"""Update scanner_ip set status = "Open" WHERE id = {ip[0]}""")
        connection.commit()

        cursor.execute(f"""Update scanner_ip set open_ports = "{open_ports}" WHERE id = {ip[0]}""")
        connection.commit()

    elif 1 <= len(open_ports) <= 10:
        with open(f'{log_dir_path}{ip[1]}.log', 'w') as log:
            log.write(','.join(open_ports))

        cursor.execute(f"""Update scanner_ip set status = "Open" WHERE id = {ip[0]}""")
        connection.commit()

        cursor.execute(f"""Update scanner_ip set open_ports = "{','.join(open_ports)}" WHERE id = {ip[0]}""")
        connection.commit()
    else:
        with open(f'{log_dir_path}{ip[1]}.log', 'w') as log:
            log.write('0')

        cursor.execute(f"""Update scanner_ip set status = "Close" WHERE id = {ip[0]}""")
        connection.commit()

        cursor.execute(f"""Update scanner_ip set open_ports = "0" WHERE id = {ip[0]}""")
        connection.commit()

connection.close()

# ('scanner_company',)
# ('scanner_ip',)
