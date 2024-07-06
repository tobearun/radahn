# Radahn

**Radahn** (Vulnerability Assessment Tool) is a Python-based application designed to perform network and web vulnerability assessments. The tool can scan for open ports, identify vulnerabilities, and generate comprehensive reports.

## Features

- **Network Scanning**: Detects open ports and services running on network hosts.
- **Web Vulnerability Scanning**: Scans for SQL injection vulnerabilities.
- **Result Parsing**: Parses scan results into a readable format.
- **Report Generation**: Generates detailed reports from scan results.

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/username/Radahn.git
    cd Radahn
    ```

2. **Create a Virtual Environment:**

    ```sh
    python -m venv .venv
    ```

3. **Activate the Virtual Environment:**

    - **Windows:**
      ```sh
      .venv\Scripts\activate
      ```
    - **Linux/Mac:**
      ```sh
      source .venv/bin/activate
      ```

4. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

5. **Install Nmap:**

    Ensure you have Nmap installed on your system. You can download it from [nmap.org](https://nmap.org/download.html).

## Usage

1. **Network Scan:**

    ```sh
    python main.py <network_target>
    ```

    Example:
    ```sh
    python main.py 192.168.1.1/24
    ```

2. **Web Vulnerability Scan:**

    ```sh
    python main.py <network_target> <web_target>
    ```

    Example:
    ```sh
    python main.py 192.168.1.1/24 http://example.com
    ```

## Project Structure

```plaintext
Radahn/
├── .venv/
├── scanner/
│   ├── __init__.py
│   ├── network_scanner.py
│   └── web_scanner.py
├── parser/
│   ├── __init__.py
│   └── result_parser.py
├── report/
│   ├── __init__.py
│   └── report_generator.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
