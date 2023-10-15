import subprocess
import ipaddress
import time

def check_subnet_availability(subnets, ping_interval):
    live_hosts = []  # List of live hosts
    dead_hosts = []  # List of non-responsive hosts

    for subnet in subnets:
        # Parse the IP address range
        network = ipaddress.ip_network(subnet, strict=False)
        
        # Iterate through the IP addresses in the range and check their availability
        for ip in network.hosts():
            ip_str = str(ip)
            try:
                # Use the ping command to check the host's availability with the specified ping interval
                response = subprocess.check_output(['ping', '-c', '3', '-i', str(ping_interval), ip_str])
                live_hosts.append(ip_str)
                print(f'{ip_str} is live')
            except subprocess.CalledProcessError:
                dead_hosts.append(ip_str)
                print(f'{ip_str} is not responsive')
            
            # Wait for the specified ping interval
            time.sleep(ping_interval)

    # Write the list of live hosts to a file
    with open('live_hosts.txt', 'w') as live_file:
        live_file.write('\n'.join(live_hosts))

    # Write the list of non-responsive hosts to a file
    with open('dead_hosts.txt', 'w') as dead_file:
        dead_file.write('\n'.join(dead_hosts))

# List of multiple IP address ranges to check
subnets = ['192.168.0.0/16', '10.0.0.0/24', '172.16.0.0/20']

# Set the ping interval by asking the user for input (in seconds)
ping_interval = float(input("Enter the ping interval (in seconds): "))

check_subnet_availability(subnets, ping_interval)
