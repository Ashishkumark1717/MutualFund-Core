
# Mutual Fund Data Automation Pipeline

## 📌 Overview
This project automates the extraction, transformation, and visualization of mutual fund data (AUM, SIPs, investor details) from vendor APIs to Power BI dashboards.

## 🔄 Workflow
1. **Data Extraction** (Python)
   - Scheduled daily API pulls at 6 AM
   - Covers: AUM, Portfolio, SIPs, Investor data
   - Files: `aum_fetcher.py`, `sip_fetcher.py`

2. **Data Processing** (SQL)
   - Cleans raw data and creates business-ready views
   - Key transformations: SIP/lumpsum tagging, KPI calculations
   - File: `sql_handler.py`

3. **Visualization** (Power BI)
   - Connects directly to SQL database
   - Auto-refreshes daily at 8 AM
   - Tracks: AUM trends, SIP performance, RM metrics

4. **Automation**
   - GitHub Actions for daily execution
   - Error logging and alerts

## 🛠 Setup
1. Clone repo:
   ```bash
   git clone https://github.com/yourusername/mutual-fund-automation.git
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure API keys in `config.py`

## 📂 File Structure
```
/src/
├── fetchers/          # API extraction scripts
├── sql/               # Database operations
/config.py             # Credentials
/requirements.txt      # Dependencies
```

## ⚙️ Scheduled Runs
- **6:00 AM**: Data extraction
- **7:00 AM**: SQL processing
- **8:00 AM**: Power BI refresh

> **Note**: Requires Python 3.8+, PostgreSQL, and Power BI service
```

**Key Features:**
- Uses emojis for visual scanning
- Clear workflow steps
- Minimal technical jargon
- Includes setup instructions
- Shows file structure
- Notes scheduling
