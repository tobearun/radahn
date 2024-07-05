import nmap


def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')
    results = []
    for host in nm.all_hosts():
        host_info = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'ports': []
        }
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                port_info = {
                    'port': port,
                    'state': nm[host][proto][port]['state']
                }
                host_info['ports'].append(port_info)
        results.append(host_info)
    return results
