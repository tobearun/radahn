def parse_network_scan(results):
    parsed_data = {
        'hosts': []
    }
    for result in results:
        parsed_data['hosts'].append(result)
    return parsed_data


def parse_web_scan(result):
    return {'web_scan_result': result}
