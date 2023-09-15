from datetime import datetime
import socket
import threading
import os
from sys import argv
from main.settings import BASE_DIR

import psycopg2

script, first = argv
open_ports = []
logs_path = str(BASE_DIR) + '\scanner\logs'


def create_general_log():
    logs_list = os.listdir(logs_path)
    for log in logs_list:
        with open(f'{logs_path}\{log}', 'r') as f:
            f = f.read()
            if f != '0':
                with open(f'{logs_path}\general.log', 'w') as log:
                    log.write('1')


def get_time():
    now = datetime.now()
    frmt = "%d.%m.%Y %H:%M:%S"
    time = now.strftime(frmt)
    return time


def execute(command):
    con = psycopg2.connect(dbname='scaner', user='postgres',
                           password='postgres', host='localhost')
    cur = con.cursor()
    cur.execute(command)
    try:
        fetch = cur.fetchall()
        con.commit()
        con.close()
        return fetch
    except psycopg2.ProgrammingError:
        pass
    con.commit()
    con.close()


def portscan(ip_addr, port_for_scan):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con = s.connect((ip_addr, port_for_scan))
        open_ports.append(str(port_for_scan))
        con.close()
    except TimeoutError:
        pass
    except Exception as e:
        pass


def scan_one_host(ip_addr):
    start_port = 1
    for x in range(1, 65535):
        t = threading.Thread(target=portscan, kwargs={'ip_addr': ip_addr, 'port_for_scan': start_port})
        start_port += 1
        t.start()
        if start_port == 65535:
            t.join()


def scan_from_db(ips):

    with open(f'{logs_path}\general.log', 'w') as log:
        log.write('0')

    for ip in ips:
        execute(f"""Update scanner_ip set scanning_now = 'True' WHERE id = {ip[0]}""")
        split_ports = []
        global open_ports
        open_ports = []

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

        if len(open_ports) > 0:
            open_ports = ','.join(open_ports)
            with open(f'{log_dir_path}{ip[1]}.log', 'w') as log:
                log.write(open_ports)
            execute(f"""UPDATE scanner_ip SET status = 'Open' WHERE id = {ip[0]};""")
            execute(f"""Update scanner_ip set update_time = '{get_time()}' WHERE id = {ip[0]}""")
            execute(f"""UPDATE scanner_ip SET open_ports = '{open_ports}' WHERE id = {ip[0]}""")
            execute(f"""Update scanner_ip set scanning_now = 'False' WHERE id = {ip[0]}""")
        else:
            with open(f'{log_dir_path}{ip[1]}.log', 'w') as log:
                log.write('0')
            execute(f"""Update scanner_ip set status = 'Close' WHERE id = {ip[0]}""")
            execute(f"""Update scanner_ip set update_time = '{get_time()}' WHERE id = {ip[0]}""")
            execute(f"""Update scanner_ip set open_ports = '0' WHERE id = {ip[0]}""")
            execute(f"""Update scanner_ip set scanning_now = 'False' WHERE id = {ip[0]}""")


ips = execute(f"SELECT id, name, allow_ports, open_ports FROM scanner_ip WHERE name = '{first}'")
scan_from_db(ips)
create_general_log()
