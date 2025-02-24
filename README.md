# PhD-DSO-Research

This repository hosts the code and documentation related to my PhD research on AI-driven DevSecOps, with a focus on automating compliance and security monitoring within DevOps workflows. The primary objective of this research is to integrate AI-driven tools into the software development pipeline, specifically for continuous integration/continuous deployment (CI/CD) pipelines, ensuring continuous compliance, risk management, and security.

## 📌 Current Focus

The current stage of the research revolves around:

### 1️⃣ **CVE Scanner Development**  
- Develop an automated CVE scanner that integrates with the CI/CD pipeline to identify vulnerabilities.  
- Implementing the functionality for scanning vulnerabilities from the [NVD CVE database](https://nvlpubs.nist.gov/nistpubs/).  

### 2️⃣ **Compliance Automation**  
- Automating security and compliance assessments throughout the DevSecOps lifecycle.  
- Using AI/ML models for enhanced threat detection and prediction.  

### 3️⃣ **Pipeline Integration**  
- Working towards integrating the CVE scanner, vulnerability reports, and automated security checks into a fully functioning CI/CD pipeline.  

### 4️⃣ **Risk Management Framework (RMF) Automation**  
- Integrating RMF steps into automated security and compliance checks.  

---

## 🚀 Next Steps

The following next steps are critical to continue progressing with the research:

### 1️⃣ **Expand CVE Scanner**  
- Continue improving the CVE scanner functionality to support additional threat sources.  
- Implement the full integration of the scanner into the CI/CD pipeline.  

### 2️⃣ **Develop AI/ML Models**  
- Begin training AI models for automated threat detection and prediction.  
- Use datasets from vulnerability databases and threat intelligence feeds.  

### 3️⃣ **Complete CI/CD Pipeline**  
- Design and build a functional CI/CD pipeline that supports:  
  - Continuous security checks.  
  - Compliance automation.  
  - Automated threat detection and remediation.  

### 4️⃣ **Integrate with RMF**  
- Build out automated processes to align DevSecOps practices with DoD RMF compliance standards.  

### 5️⃣ **Research Papers and Documentation**  
- Continue writing the literature review and methodology for the PhD dissertation.  
- Document each milestone and research finding in the `docs/` directory for future publication and review.  

---

## 🏗 Project Structure

- **PhD-DSO-Research/**
  - **src/** _(Source Code)_
    - **cve_scanner/** _(Automated CVE Scanning Module)_
      - `cve_scanner.py` _(Main CVE scanner script)_
      - `cve_parser.py` _(Parses NVD CVE JSON data)_
      - `dependency_checker.py` _(Scans dependencies for vulnerabilities)_
      - `requirements.txt` _(Dependencies for CVE scanner)_
      - `__init__.py`
    - **compliance/** _(Compliance & Security Automation)_
      - `policy_checker.py` _(Checks compliance policies)_
      - `rmf_mapper.py` _(Maps vulnerabilities to RMF/NIST standards)_
      - `compliance_reporter.py` _(Generates compliance audit reports)_
      - **policies/** _(Predefined compliance rules in YAML/JSON)_
      - `__init__.py`
    - **threat_detection/** _(AI-powered Threat Detection)_
      - `ml_model.py` _(Machine learning model for risk analysis)_
      - `data_preprocessor.py` _(Prepares data for ML training)_
      - `threat_analysis.py` _(AI-driven threat prediction script)_
      - **datasets/** _(Stores training datasets)_
      - `__init__.py`
    - **ci_cd_integration/** _(Security & Compliance in CI/CD)_
      - `security_gate.py` _(Fails builds if security issues are detected)_
      - `ci_cd_hooks.py` _(Hooks for GitHub Actions/GitLab CI)_
      - `__init__.py`
  - **tests/** _(Unit & Integration Tests)_
    - `test_cve_scanner.py` _(Unit tests for CVE Scanner)_
    - `test_compliance.py` _(Unit tests for Compliance Automation)_
    - `test_ml_model.py` _(Unit tests for AI-based threat detection)_
    - `__init__.py`
  - **docs/** _(Research Documentation)_
    - `literature_review.md` _(Literature Review for PhD Research)_
    - `methodology.md` _(Methodology of AI-Driven DevSecOps)_
    - `compliance_mapping.md` _(Mapping vulnerabilities to RMF/NIST)_
    - `ci_cd_security.md` _(Security practices for CI/CD)_
    - `threat_detection.md` _(AI and ML-based threat detection)_
  - **configs/** _(Configuration Files)_
    - `settings.yaml` _(Configurations for scanning thresholds)_
    - `model_config.yaml` _(ML model hyperparameters)_
  - **.github/** _(GitHub Actions for CI/CD automation)_
    - **workflows/**
      - `security_scan.yml` _(CI/CD security scan automation)_
      - `cve_check.yml` _(Runs CVE scanner on each commit)_
  - `requirements.txt` _(Dependencies)_
  - `main.py` _(Entry point for testing components)_
  - `README.md` _(Project Overview & Setup Guide)_
  - `LICENSE` _(Open-source license information)_
  - `.gitignore` _(Ignore unnecessary files like datasets)_
---

## 🚀 Setup & Installation

### 1️⃣ **Clone the repository**

git clone https://github.com/yojimbo256/PhD-DSO-Research.git
cd PhD-DSO-Research

### 2️⃣ Create a virtual environment(recommended for isolation):

python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

### 3️⃣ Install dependencies:

pip install -r requirements.txt

### 4️⃣ Run CVE Scanner (as an example):

python src/cve_scanner/cve_scanner.py

---

## 📜 License

This project is licensed under the **MIT License**.

Copyright (c) 2025 Keith Alexander

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

All copies or substantial portions of the Software must include the above copyright notice and this permission notice.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
