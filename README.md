**Host Availability Checker**

**Introduction:**
The "Host Availability Checker" script is a Python tool designed to check the availability of hosts within specified IP address ranges. It pings a range of IP addresses and records which hosts are responsive (alive) and which are not (unresponsive). The results are saved in separate files for easy reference.

**Key Features:**
- Check the availability of multiple hosts in specified IP address ranges.
- Save a list of responsive hosts to a file.
- Save a list of unresponsive hosts to a file.
- Set custom ping intervals to control the frequency of checks.
- Customize IP address ranges to suit your needs.

---

**Usage Tutorial: Host Availability Checker**

**Step 1: Prepare Your Environment**
Make sure you have Python installed on your system. You can download Python from the official website (https://www.python.org/). This script is compatible with Python 3.

**Step 2: Download the Script**
Download the script from the GitHub repository at [this link](https://raw.githubusercontent.com/YuanLiuchang/HostAvailabilityChecker/main/BreadcrumbsHostAvailabilityChecker.py) and save it in your local directory.

**Step 3: Customize IP Address Ranges**
Open the script in a text editor. You can customize the list of IP address ranges by editing the `subnets` variable. Add or remove IP address ranges as needed, following this format:

```python
subnets = ['192.168.0.0/16', '10.0.0.0/24', '172.16.0.0/20']
```

Simply add or modify the address ranges to suit your specific requirements.

**Step 4: Run the Script**
Open your command-line terminal and navigate to the directory where the script is located. Use the following command to execute the script:

```bash
python BreadcrumbsHostAvailabilityChecker.py
```

The script will prompt you to enter the ping interval in seconds.

**Step 5: View the Results**
The script will check the availability of hosts and save the results to two text files:
- `live_hosts.txt`: Contains a list of responsive hosts.
- `dead_hosts.txt`: Contains a list of unresponsive hosts.

You can open these files to view the lists of hosts accordingly.

That's it! The "Host Availability Checker" script simplifies the process of checking the availability of hosts within specified IP address ranges and provides an easy-to-use tool for this purpose. You can customize the IP address ranges in the script to meet your specific needs.
