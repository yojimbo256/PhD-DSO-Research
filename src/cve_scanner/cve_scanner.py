import json
import requests

NVD_API_URL = "https://services.nvd.nist.gov/rest/json/cves/1.1"

def fetch_cve_data():
    """Fetch latest CVEs from NVD"""
    response = requests.get(f"{NVD_API_URL}?resultsPerPage=10")
    if response.status_code == 200:
        return response.json()
    return None

def scan_vulnerabilities():
    """Basic function to process CVE data"""
    cve_data = fetch_cve_data()
    if cve_data:
        for item in cve_data["result"]["CVE_Items"]:
            print(f"ID: {item['cve']['CVE_data_meta']['ID']} - {item['cve']['description']['description_data'][0]['value']}")

if __name__ == "__main__":
    scan_vulnerabilities()

