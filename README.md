# Threat Intelligence Dashboard

## Overview
This project uses the VirusTotal API to collect, analyze, and visualize threat intelligence data for multiple domains. Skills involved: API integration, data analysis, and visualization.

## Features
- Fetches domain analysis data using the VirusTotal API.
- Summarizes results, including malicious, suspicious, and harmless counts.
- Visualizes the data as a bar chart.

### **Data Overview**
The bar chart visualization and `domain_data.csv` file provide a breakdown of VirusTotal's analysis for each queried domain. The data includes the following categories:

1. **Malicious**: The number of antivirus engines that flagged the domain as harmful.
2. **Suspicious**: The number of engines that flagged the domain as potentially harmful or questionable.
3. **Harmless**: The number of engines that determined the domain was safe.
4. **Undetected**: The number of engines that did not return a definitive result (neither flagged nor safe).
5. **Reputation**: An aggregated score from VirusTotal that indicates the domain's overall trustworthiness:
   - **Positive Scores**: Indicate good reputation (domain is widely considered safe).
   - **Negative Scores**: Indicate bad reputation (domain is flagged for malicious activity or risks).
   - **Zero or "Unknown"**: Indicates insufficient data to assess the domain's reputation.

### **Data Location**
All the collected data is stored in the `data/domain_data.csv` file, which serves as the source for the bar chart visualization.


## Technologies Used
- **Python**
- **Libraries**:
  - `requests` for API interaction.
  - `pandas` for data analysis.
  - `matplotlib` for visualizations.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ThreatDashboard.git
   cd ThreatDashboard

2. Add Your VirusTotal API Key:
   - Create a file named `virustotal_api_key.txt` in the project folder.
   - Paste your API key into the file and save it.
   - **Note**: The file is excluded from version control for security using `.gitignore`.


3. Create and activate a virtual environment:
    Windows:
        python -m venv venv
        venv\Scripts\activate
    Mac/Linux:
        python3 -m venv venv
        source venv/bin/activate

4. Install dependencies:
    pip install -r requirements.txt

5. Run the scripts:
    Fetch Data:
        python fetch_data.py
    Visualize Data:
        python visualize_data.py


Project Results
The project collected data for multiple domains and summarized their analysis stats. A bar chart was generated to visualize the proportion of malicious, suspicious, harmless, and undetected domains.


Future Improvements
-Automate data updates with a scheduler (e.g., using cron or Task Scheduler).
-Add more visualizations or interactivity with tools like Dash or Plotly.
-Expand the project to include additional data sources such as AbuseIPDB.

-Acknowledgments
Data Source: VirusTotal API
