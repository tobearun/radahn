import requests


def scan_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(f"{url}?id={payload}")
    if "SQL Syntax" in response.text:
        return "Potential SQL Injection vulnerability found!"
    return "No SQL injection vulnerability detected."
