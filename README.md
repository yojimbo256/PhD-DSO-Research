# PhD-DSO-Research

This repository hosts the code and documentation related to my PhD research on AI-driven DevSecOps, with a focus on automating compliance and security monitoring within DevOps workflows. The primary objective of this research is to integrate AI-driven tools into the software development pipeline, specifically for continuous integration/continuous deployment (CI/CD) pipelines, ensuring continuous compliance, risk management, and security.

## Current Focus

The current stage of the research revolves around:

1. **CVE Scanner Development**: 
   - Develop an automated CVE scanner that integrates with the CI/CD pipeline to identify vulnerabilities.
   - Implementing the functionality for scanning vulnerabilities from the [NVD CVE database](https://nvlpubs.nist.gov/nistpubs/).
   
2. **Compliance Automation**:
   - Automating security and compliance assessments throughout the DevSecOps lifecycle.
   - Using AI/ML models for enhanced threat detection and prediction.

3. **Pipeline Integration**:
   - Working towards integrating the CVE scanner, vulnerability reports, and automated security checks into a fully functioning CI/CD pipeline.

4. **Risk Management Framework (RMF) Automation**:
   - Integrating RMF steps into automated security and compliance checks.

## Next Steps

The following next steps are critical to continue progressing with the research:

1. **Expand CVE Scanner**:
   - Continue improving the CVE scanner functionality to support additional threat sources.
   - Implement the full integration of the scanner into the CI/CD pipeline.

2. **Develop AI/ML Models**:
   - Begin training AI models for automated threat detection and prediction.
   - Use datasets from vulnerability databases and threat intelligence feeds.

3. **Complete CI/CD Pipeline**:
   - Design and build a functional CI/CD pipeline that supports:
     - Continuous security checks.
     - Compliance automation.
     - Automated threat detection and remediation.
   
4. **Integrate with RMF**:
   - Build out automated processes to align DevSecOps practices with DoD RMF compliance standards.
   
5. **Research Papers and Documentation**:
   - Continue writing the literature review and methodology for the PhD dissertation.
   - Document each milestone and research finding in the `docs/` directory for future publication and review.

## Repository Structure

- `CVE_scanner.py`: Contains the code for scanning CVEs and identifying known vulnerabilities.
- `nvdCVE-1.1-recent.json`: Stores the most recent CVE data for testing.
- `requirements.txt`: Python dependencies for the CVE scanner and other modules.
- `vuln_requirements.txt`: Lists dependencies specific to vulnerability management.
- `venv/`: Python virtual environment containing necessary packages.
- `.gitignore`: Lists files and directories to be ignored in version control.
  
## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yojimbo256/PhD-DSo-Research.git
   cd PhD-DSo-Research
