import json
import os
import csv

# Path to Local NVD JSON Database
CVE_DATABASE_PATH = "/home/coder/PhD-DSO-Research/nvdcve-1.1-recent.json"

def load_cve_database(json_file):
    """Load CVE data from a local JSON file."""
    if not os.path.exists(json_file):
        print(f"Error: CVE database {json_file} not found.")
        return []
    
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("CVE_Items", [])

def determine_criticality(cve_item):
    """Determine the criticality based on CVSS score."""
    if "impact" in cve_item:
        cvss_score = cve_item["impact"].get("baseMetricV2", {}).get("score", 0)
        if cvss_score >= 9.0:
            return "Critical"
        elif cvss_score >= 7.0:
            return "High"
        elif cvss_score >= 4.0:
            return "Medium"
        else:
            return "Low"
    return "Unknown"

def check_cve_local(package_name, cve_data):
    """Check if a package has known vulnerabilities in the offline dataset."""
    vulnerabilities = []
    for item in cve_data:
        description = item["cve"]["description"]["description_data"][0]["value"]
        cve_id = item["cve"]["CVE_data_meta"]["ID"]
        criticality = determine_criticality(item)
        
        if package_name.lower() in description.lower():
            vulnerabilities.append((cve_id, description, criticality))
    return vulnerabilities

def scan_dependencies(requirements_file, cve_data):
    """Read dependencies from requirements.txt and check for vulnerabilities."""
    if not os.path.exists(requirements_file):
        print("Error: requirements.txt file not found.")
        return []
    
    with open(requirements_file, "r") as file:
        dependencies = [line.strip().split("==")[0] for line in file if line.strip() and not line.startswith("#")]
    
    results = []
    for package in dependencies:
        print(f"Checking {package} for vulnerabilities...")
        cves = check_cve_local(package, cve_data)
        for cve_id, summary, criticality in cves:
            results.append([package, cve_id, summary, criticality])
    
    return results

def save_results_csv(results, output_file="cve_report.csv"):
    """Save CVE scan results to a CSV file."""
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Package", "CVE ID", "Description", "Criticality"])
        writer.writerows(results)
    print(f"✅ CVE report saved to {output_file}")

def save_results_json(results, output_file="cve_report.json"):
    """Save CVE scan results to a JSON file."""
    with open(output_file, "w") as file:
        json.dump([{ "package": r[0], "cve_id": r[1], "description": r[2], "criticality": r[3] } for r in results], file, indent=4)
    print(f"✅ CVE report saved to {output_file}")

# Example Usage
if __name__ == "__main__":
    cve_data = load_cve_database(CVE_DATABASE_PATH)  # Load local CVE database
    requirements_file = "requirements.txt"  # Change if necessary
    results = scan_dependencies(requirements_file, cve_data)
    
    if results:
        save_results_csv(results)
        save_results_json(results)
    else:
        print("No vulnerabilities found.")
