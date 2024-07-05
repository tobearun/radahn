import sys
from scanner.network_scanner import scan_network
from scanner.web_scanner import scan_sql_injection
from parser.result_parser import parse_network_scan, parse_web_scan
from report.report_generator import generate_report


def main():
    parsed_network_results = None
    parsed_web_results = None

    if len(sys.argv) < 2:
        print("Usage: python main.py <network_target> [<web_target>]")
        return

    target_network = sys.argv[1]
    target_web = sys.argv[2] if len(sys.argv) > 2 else None

    if target_network:
        network_results = scan_network(target_network)
        parsed_network_results = parse_network_scan(network_results)
        print("Network scan results:")
        print(parsed_network_results)

    if target_web:
        web_results = scan_sql_injection(target_web)
        sql_injection_results = scan_sql_injection(web_results)
        parsed_web_results = parse_web_scan(web_results)
        report = generate_report(parsed_network_results)
        print("Web scan results:")
        print(report)


if __name__ == "__main__":
    main()
