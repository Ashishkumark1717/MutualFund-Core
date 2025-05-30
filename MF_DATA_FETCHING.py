import requests
import json
import pandas as pd
# def generate_token():
url = "https://mf.kunvarjiwealth.com/fcapi/account/login"
headers = {
    "Authorization": "Bearer kunvarji_9361:6Ig5@ew7RfzV3HkkF7sUA#1h2tC7uk",
    "Cookie": "ARRAffinity=d76b35f27e1c73417a9662889f61eda3669ef8adcfe16f7d2bb60b68e17317c8; ARRAffinitySameSite=d76b35f27e1c73417a9662889f61eda3669ef8adcfe16f7d2bb60b68e17317c8",
    "Content-Type": "application/json"
}
data = {
    "LoginName": "mfkunvarji@kunvarji.com",
    "Password": "Mfkunvarji@02",
    "LoginUserType": 3,
    "RouteKey": "",
    "AuthSource": "",
    "expiresIn": 3600
}
response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    # print("Token Response:", response.json())
    api_response = response.json()
    # df = pd.json_normalize(api_response['Data']['AccessToken'])
    # print(df)
    generate_token = api_response['Data']['AccessToken']
    # print(generate_token)
else:
    print("Error:", response.status_code, response.text)
# if __name__ == "__main__":
#     generate_token()
print(generate_token)
# INVESTOR MASTER DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM INVESTOR_MASTER"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/investor/list"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        investor_data = json_data['Data']
        df = pd.DataFrame(investor_data)
        # return response.json()
    else:
        print(f"Error fetching data for investor {investor_id}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('INVESTOR_MASTER', engine, if_exists='append', index=False)
    print("Data successfully inserted into SQL table")
    
except Exception as e:
    print(f"Error occurred: {e}")
# STOP SIPs DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM CANCELLED_SIP_DATA"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/investor/mf/sip-ceased-report"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}
payload = json.dumps({
    "InvestorId": 0,
  "FromDate": "1990-04-29T04:49:26.381Z",
  "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
  "RefKey": "string"
})
try:
    # Fetch data from API
    response = requests.post(url, headers=headers, data = payload)
    if response.status_code == 200:
        json_data = response.json()
        investor_data = json_data['Data']
        df = pd.DataFrame(investor_data)
        # return response.json()
    else:
        print(f"Error fetching data for investor {investor_id}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('CANCELLED_SIP_DATA', engine, if_exists='append', index=False)
    df.to_excel('STOP_SIP.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    
except Exception as e:
    print(f"Error occurred: {e}")
# EXPIRED SIPs DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM EXPIRED_SIP_DATA"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/investor/mf/sip-expiry-report"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}
payload = json.dumps({
    "InvestorId": 0,
  "FromDate": "1990-04-29T04:49:26.381Z",
  "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
  "RefKey": "string"
})
try:
    # Fetch data from API
    response = requests.post(url, headers=headers, data = payload)
    if response.status_code == 200:
        json_data = response.json()
        investor_data = json_data['Data']
        df = pd.DataFrame(investor_data)
        # return response.json()
    else:
        print(f"Error fetching data for investor {investor_id}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('EXPIRED_SIP_DATA', engine, if_exists='append', index=False)
    df.to_excel('EXPIRED_SIP_DATA.xlsx', index=False)
    print("Data successfully inserted into Excel File")
    print("Data successfully inserted into SQL table")
    
except Exception as e:
    print(f"Error occurred: {e}")
# BOUNCE SIPs DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM BOUNCE_SIP_DATA"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/investor/mf/sip-bounce-report"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}
payload = json.dumps({
    "InvestorId": 0,
  "FromDate": "1990-04-29T04:49:26.381Z",
  "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
  "arnNumber": "45111",
  "RefKey": "string"
})
try:
    # Fetch data from API
    response = requests.post(url, headers=headers, data = payload)
    if response.status_code == 200:
        json_data = response.json()
        investor_data = json_data['Data']
        df = pd.DataFrame(investor_data)
        # return response.json()
    else:
        print(f"Error fetching data for investor {investor_id}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('BOUNCE_SIP_DATA', engine, if_exists='append', index=False)
    df.to_excel('BOUNCE_SIP_DATA.xlsx', index=False)
    print("Data successfully inserted into Excel File")
    print("Data successfully inserted into SQL table")
    
except Exception as e:
    print(f"Error occurred: {e}")
# INVESTOR AUM DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM INVESTOR_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/aum-report/investor-wise"
payload = json.dumps({
   "AsOnDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
  "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        investor_aum = json_data['Data']['Table']
        df = pd.DataFrame(investor_aum)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Investor_Name}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('INVESTOR_AUM', engine, if_exists='append', index=False)
    df.to_excel('INVESTOR_AUM.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# RM AUM DATA FETCHING 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json

# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM RM_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/aum-report/rm-wise"
payload = json.dumps({
   "AsOnDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
  "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        rm_aum = json_data['Data']['Table']
        df = pd.DataFrame(rm_aum)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Emp_Code}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    df.to_sql('RM_AUM', engine, if_exists='append', index=False)
    df.to_excel('RM_AUM.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# SIP ALLOCATION TABLE 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json


# import requests
# import json

# url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-collection-report"

# payload = json.dumps({
#   "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
#   "ReportWise": "BRANCH_WISE",
#   "RefKey": "string"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': f'Bearer {generate_token}',
#   'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
# }



# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

# with engine.begin() as conn:
#     conn.execute(text("DELETE FROM RM_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-collection-report"
payload = json.dumps({
    "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "ReportWise": "RM_WISE",
    "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        SIP_DATA = json_data['Data']
        df = pd.DataFrame(SIP_DATA)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Name}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    # df.to_sql('RM_AUM', engine, if_exists='append', index=False)
    df.to_excel('SIP_DATA.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# SIP ALLOCATION TABLE 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json


# import requests
# import json

# url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-collection-report"

# payload = json.dumps({
#   "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
#   "ReportWise": "BRANCH_WISE",
#   "RefKey": "string"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': f'Bearer {generate_token}',
#   'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
# }



# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

# with engine.begin() as conn:
#     conn.execute(text("DELETE FROM RM_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-allocation"
payload = json.dumps({
    "FromDate": "1990-04-24T09:24:06.737Z",
    "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    "ReportWise": "RM_WISE",
    "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        SIP_DATA = json_data['Data']
        df = pd.DataFrame(SIP_DATA)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Employee_Name}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    # df.to_sql('RM_AUM', engine, if_exists='append', index=False)
    df.to_excel('SIP_DATA_RM_WISE.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# SIP COLLECTION TABLE 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json


# import requests
# import json

# url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-collection-report"

# payload = json.dumps({
#   "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
#   "ReportWise": "BRANCH_WISE",
#   "RefKey": "string"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': f'Bearer {generate_token}',
#   'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
# }



# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

# with engine.begin() as conn:
#     conn.execute(text("DELETE FROM RM_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/collection-report/investor-wise"
payload = json.dumps({
    "FromDate": "1990-04-24T09:24:06.737Z",
    "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    # "ReportWise": "RM_WISE",
    "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        SIP_DATA = json_data['Data']
        df = pd.DataFrame(SIP_DATA)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Investor_Name}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    # df.to_sql('RM_AUM', engine, if_exists='append', index=False)
    df.to_excel('SIP_INVESTED_AMOUNT_INVESTOR_WISE.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# SIP COLLECTION TABLE 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
import json


# import requests
# import json

# url = "https://mf.kunvarjiwealth.com/fcapi/report/mf/sip-collection-report"

# payload = json.dumps({
#   "Date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
#   "ReportWise": "BRANCH_WISE",
#   "RefKey": "string"
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': f'Bearer {generate_token}',
#   'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
# }



# SQL Server connection
# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

# with engine.begin() as conn:
#     conn.execute(text("DELETE FROM RM_AUM"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/collection-report/rm-wise"
payload = json.dumps({
    "FromDate": "1990-04-24T09:24:06.737Z",
    "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
    # "ReportWise": "RM_WISE",
    "RefKey": "string"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers,data = payload)
    if response.status_code == 200:
        json_data = response.json()
        SIP_DATA = json_data['Data']
        df = pd.DataFrame(SIP_DATA)
        # return response.json()
    else:
        print(f"Error fetching data for investor {Investor_Name}: {response.status_code}")
        # return None  # Raise error for bad status codes
    
    # Convert to DataFrame
    
    
    # Insert into SQL table
    # df.to_sql('RM_AUM', engine, if_exists='append', index=False)
    df.to_excel('SIP_INVESTED_AMOUNT_RM_WISE.xlsx', index=False)
    print("Data successfully inserted into SQL table")
    print("Data successfully inserted into Excel Sheet")
    
except Exception as e:
    print(f"Error occurred: {e}")
# MF_ORDER BOOK
import requests
import pandas as pd
import json
from datetime import datetime
import sqlalchemy
from sqlalchemy import  text
import threading
from queue import Queue
import time

# ✅ SQL Server connection details
server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# ✅ Create SQLAlchemy engine
engine = sqlalchemy.create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)



with engine.begin() as conn:
    conn.execute(text("DELETE FROM MF_ORDER_BOOK"))

# API Configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/order-book/systematic"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

# Threading configuration
MAX_THREADS = 50  # Adjust based on API rate limits
TOKEN_REFRESH_INTERVAL = 1800  # 30 minutes in seconds
token_lock = threading.Lock()
last_token_refresh = time.time()

class SIPFetcher:
    def __init__(self):
        self.failed_ids = []
        self.success_count = 0
        self.lock = threading.Lock()
    
    def refresh_token_if_needed(self):
        """Check and refresh token if expired"""
        global headers, last_token_refresh
        
        with token_lock:
            current_time = time.time()
            if current_time - last_token_refresh > TOKEN_REFRESH_INTERVAL:
                print("\nRefreshing token...")
                # Add your token refresh logic here
                # new_token = get_new_token()
                # headers['Authorization'] = f'Bearer {new_token}'
                last_token_refresh = current_time
    
    def fetch_data(self, investor_id):
        """Fetch data from API for a single investor"""
        self.refresh_token_if_needed()
        
        payload = json.dumps({
            "FromDate": "1990-04-11T04:08:25.394Z",
            "ToDate": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "InvestorId": investor_id,
            "RefKey": "string"
        })
        
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=30)
            
            if response.status_code == 401:  # Token expired
                with token_lock:
                    print("Token expired, refreshing...")
                    # Add token refresh logic here
                    # new_token = get_new_token()
                    # headers['Authorization'] = f'Bearer {new_token}'
                    last_token_refresh = time.time()
                    response = requests.post(url, headers=headers, data=payload, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                with self.lock:
                    self.failed_ids.append((investor_id, f"HTTP {response.status_code}"))
                return None
                
        except Exception as e:
            with self.lock:
                self.failed_ids.append((investor_id, str(e)))
            return None
    
    def normalize_and_save(self, api_response, investor_id):
        """Normalize API response and save to database"""
        try:
            if not api_response or 'Data' not in api_response:
                with self.lock:
                    self.failed_ids.append((investor_id, "No data in response"))
                return None
                
            df = pd.json_normalize(api_response['Data'])
            
            # Your existing normalization logic
            date_columns = ['RegDate', 'StartDate', 'EndDate']
            for col in date_columns:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
            
            df.replace(['', 'NA', 'N/A', None], pd.NA, inplace=True)
            numeric_cols = ['Amount', 'OrderID']
            for col in numeric_cols:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            df.columns = [col.lower() for col in df.columns]
            
            # Save to database
            with self.lock:
                df.to_sql("MF_ORDER_BOOK", con=engine, if_exists="append", index=False, chunksize = 1000)
                self.success_count += 1
                if self.success_count % 100 == 0:
                    print(f"Processed {self.success_count} investors...")
            
            return df
            
        except Exception as e:
            with self.lock:
                self.failed_ids.append((investor_id, f"Normalization error: {str(e)}"))
            return None

def worker(fetcher, queue):
    """Thread worker function"""
    while not queue.empty():
        investor_id = queue.get()
        
        # Fetch data
        api_response = fetcher.fetch_data(investor_id)
        
        # Process if successful
        if api_response:
            fetcher.normalize_and_save(api_response, investor_id)
        
        queue.task_done()

def main():
    # Load investor IDs
    investor_df = pd.read_sql("SELECT Id FROM INVESTOR_MASTER", engine)
    investor_ids = investor_df['Id'].tolist()
    
    # Create queue and add all investor IDs
    task_queue = Queue()
    for investor_id in investor_ids:
        task_queue.put(investor_id)
    
    # Initialize fetcher
    fetcher = SIPFetcher()
    
    # Create and start worker threads
    threads = []
    for _ in range(MAX_THREADS):
        t = threading.Thread(target=worker, args=(fetcher, task_queue))
        t.start()
        threads.append(t)
    
    # Wait for all tasks to complete
    task_queue.join()
    
    # Stop workers
    for _ in range(MAX_THREADS):
        task_queue.put(None)
    for t in threads:
        t.join()
    
    # Generate report
    print("\nProcessing complete!")
    print(f"Successfully processed: {fetcher.success_count}")
    print(f"Failed to process: {len(fetcher.failed_ids)}")
    
    if fetcher.failed_ids:
        print("\nFirst 10 failed IDs:")
        for investor_id, error in fetcher.failed_ids[:10]:
            print(f"ID: {investor_id} - Error: {error}")
        
        # Save failed IDs to file
        failed_df = pd.DataFrame(fetcher.failed_ids, columns=['InvestorID', 'Error'])
        failed_df.to_csv('failed_investors.csv', index=False)
        print("\nFull list of failed IDs saved to 'failed_investors.csv'")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"\nTotal execution time: {time.time() - start_time:.2f} seconds")
# TRANSACTION BOOK
import requests
import json
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import sqlalchemy
from sqlalchemy import create_engine, text
import os

server = '192.168.100.55'
database = 'Wealthone'
username = 'aruhat'
password = 'aruhat'

# Configuration
BASE_URL = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/investor/transaction-report"
AUTH_TOKEN = f"Bearer {generate_token}"
START_YEAR = 1996
END_YEAR = datetime.now().year  # Current year
OUTPUT_EXCEL = "mutual_fund_data.xlsx"
SQL_CONNECTION_STRING = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
# sqlalchemy.create_engine(
                            # f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
  # )  # Change to your SQL connection


with engine.begin() as conn:
    conn.execute(text("DELETE FROM MUTUALFUND_TRANSACTIONS"))
# Headers setup
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTH_TOKEN,
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

def fetch_year_data(year):
    """Fetch data for a specific year"""
    from_date = f"{year}-01-01T00:00:00.000Z"
    to_date = f"{year+1}-01-01T00:00:00.000Z" if year < END_YEAR else datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
    
    payload = json.dumps({
        "ReportType": "0",
        "FromDate": from_date,
        "ToDate": to_date,
        "InvestorId": 0,
        "RefKey": "string"
    })
    
    try:
        response = requests.post(BASE_URL, headers=headers, data=payload)
        response.raise_for_status()
        data = response.json()
        
        if data.get('Data'):
            df = pd.json_normalize(data['Data'])
            df['year'] = year
            return df
        else:
            print(f"No data for year {year}")
            return None
    except Exception as e:
        print(f"Error fetching data for {year}: {str(e)}")
        return None

def fetch_all_data():
    """Fetch data for all years using multi-threading"""
    all_data = []
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all year requests
        future_to_year = {
            executor.submit(fetch_year_data, year): year 
            for year in range(START_YEAR, END_YEAR + 1)
        }
        
        # Process completed requests
        for future in as_completed(future_to_year):
            year = future_to_year[future]
            try:
                result = future.result()
                if result is not None:
                    all_data.append(result)
                    print(f"Successfully processed year {year}")
            except Exception as e:
                print(f"Error processing year {year}: {str(e)}")
    
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    return pd.DataFrame()

def save_to_excel(df, filename):
    """Save DataFrame to Excel"""
    if not df.empty:
        df.to_excel(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save to Excel")

def save_to_sql(df, table_name="MUTUALFUND_TRANSACTIONS"):
    """Save DataFrame to SQL database"""
    if not df.empty:
        try:
            engine = create_engine(SQL_CONNECTION_STRING)
            df.to_sql(table_name, engine, if_exists='append', index=False)
            print(f"Data saved to SQL table {table_name}")
        except Exception as e:
            print(f"Error saving to SQL: {str(e)}")
    else:
        print("No data to save to SQL")

def main():
    print(f"Fetching data from {START_YEAR} to {END_YEAR}...")
    
    # Fetch all data
    combined_df = fetch_all_data()
    
    if not combined_df.empty:
        # Save to Excel
        save_to_excel(combined_df, OUTPUT_EXCEL)
        
        # Save to SQL
        save_to_sql(combined_df)
        
        print("Process completed successfully!")
    else:
        print("No data was fetched. Please check your connection and parameters.")

if __name__ == "__main__":
    main()
# MF_LIVE 
import requests
import pandas as pd
from sqlalchemy import create_engine, text
import json

# SQL Server connection
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM MF_LIVE"))


# API configuration
url = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/sip-report/live"
payload = {
    "InvestorId": 0,
    "RefKey": "string"
}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {generate_token}',
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

try:
    # Fetch data from API
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        json_data = response.json()
        investor_data = json_data['Data']
        df = pd.DataFrame(investor_data)
        # Process your DataFrame here
        # df.to_sql('MF_LIVE', engine, if_exists='append', index=False)
        # print("Data successfully processed")
        # print(df)
        df.to_excel('MF_LIVE.xlsx', index = False)
        print('Successfully Created Excel File')
        df.to_sql('MF_LIVE', engine, if_exists = 'append', index = False)
        print('Successfully Inserted into SQL Table')
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")
    
except Exception as e:
    print(f"Error occurred: {e}")
# INVESTOR MATCHES 
import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime
from datetime import timedelta

# Database configuration
server = '192.168.100.55'
database = 'WEALTHONE'
username = 'aruhat'
password = 'aruhat'

# Create database connection
engine = create_engine(
    f"mssql+pyodbc://{username}:{password}@{server}/{database}?"
    "driver=ODBC+Driver+17+for+SQL+Server"
)

with engine.begin() as conn:
    conn.execute(text("DELETE FROM INVESTOR_MATCHES"))


try:
    # Fetch order data with date conversion
    order_df = pd.read_sql("""
        SELECT 
            regno, 
            investorcode, 
            amcid, 
            foliono, 
            CAST(LEFT(registrationdate, CHARINDEX('T', registrationdate) - 1) AS DATE) AS regdate,
            amount
        FROM mf_live 
      
        WHERE MANDATESTATUS = 'APPROVED'
        OR MANDATESTATUS = ''

       
    """, engine)
    
    if order_df.empty:
        print("No accepted orders found")
    else:
        # Fetch transaction data
        trans_df = pd.read_sql("""
            SELECT 
                investorcode, 
                amcid, 
                CASE 
                    WHEN CHARINDEX('/', foliono ) > 0 THEN LEFT(foliono, CHARINDEX('/', foliono) -1)
                    ELSE foliono
                    END AS foliono, 
                trandate
            FROM MUTUALFUND_TRANSACTIONS
            
        """, engine)
        
        # Convert dates
        order_df['regdate'] = pd.to_datetime(order_df['regdate']).dt.normalize()
        trans_df['trandate'] = pd.to_datetime(trans_df['trandate']).dt.normalize()
        
        # Process matches
        results = []
        for _, order in order_df.iterrows():
            # Create matching conditions
            conditions = [
                trans_df['investorcode'] == order['investorcode'],
                trans_df['amcid'] == order['amcid']
            ]
            
            # Add folio condition if exists
            if pd.notna(order['foliono']) and str(order['foliono']).strip():
                folio_str = str(order['foliono']).strip()
                conditions.append(trans_df['foliono'].apply(lambda x: str(x).strip() == folio_str))
            
            # Find matches
            matches = trans_df[pd.concat(conditions, axis=1).all(axis=1)]
            if pd.notna(order['regdate']):
                matches = matches[matches['trandate'] >= order['regdate']]
            
            # Store results
            result = {
                'regno': order['regno'],
                'investorcode': order['investorcode'],
                'amcid': order['amcid'],
                'foliono': order['foliono'],
                'regdate': order['regdate'],
                'has_match': not matches.empty,
                'amt': order['amount'],
                'first_match_date': matches['trandate'].min() if not matches.empty else None,
                # 'last_match_date': matches['trandate'].max() if not matches.empty else None,
                'execution_time': datetime.now()
            }
            results.append(result)
        
        # Create DataFrame and save to SQL
        result_df = pd.DataFrame(results)
        if not result_df.empty:
            result_df.to_sql(
                'INVESTOR_MATCHES',
                engine,
                if_exists='append',
                index=False
            )
            print(f"Inserted {len(result_df)} records into SQL")
            
            # Also save to Excel
            result_df.to_excel("results.xlsx", index=False)
            print("Saved results to Excel")

except Exception as e:
    print(f"Error occurred: {str(e)}")
finally:
    engine.dispose()
    print("Processing completed")
# portfolio data api real 
import requests
import json
import pandas as pd
from sqlalchemy import create_engine, types, text
from datetime import datetime
import pytz
import concurrent.futures
from threading import Lock
import time


server = '192.168.100.55'
database = 'WEALTHONE'
username = 'aruhat'
password = 'aruhat'
# engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

# API setup
API_URL = "https://mf.kunvarjiwealth.com/fcapi/reports/mf/portfolio"
# Configuration
AUTH_TOKEN = f"Bearer {generate_token}"
DB_CONNECTION_STRING = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"  # e.g., "mysql+pymysql://user:password@host/db"
EXCEL_FILE_PATH = "investor_portfolio.xlsx"
# Configuration

with engine.begin() as conn:
    conn.execute(text("DELETE FROM investor_portfolio_data"))
    
SQL_TABLE_NAME = "investor_portfolio_data"
MAX_THREADS = 50  # Adjust based on your API rate limits
REQUEST_TIMEOUT = 30  # seconds
RETRY_COUNT = 3  # Number of retries for failed requests

# Headers for API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTH_TOKEN,
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

# Global variables for thread-safe operations
data_lock = Lock()
combined_data = pd.DataFrame()

def get_investor_ids():
    """Fetch investor IDs from investor_master table"""
    engine = create_engine(DB_CONNECTION_STRING)
    query = "SELECT DISTINCT Id FROM investor_master"
    df = pd.read_sql(query, engine)
    return df['Id'].tolist()

def fetch_single_investor_data(investor_id):
    """Fetch data from API for a single investor with retry logic"""
    as_on_date = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    payload = json.dumps({
        "IncludeZeroHolding": True,
        "AsOnDate": as_on_date,
        "InvestorId": investor_id,
        "RefKey": "string"
    })
    
    for attempt in range(RETRY_COUNT):
        try:
            response = requests.post(
                API_URL,
                headers=headers,
                data=payload,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            data = response.json()
            
            # Convert to DataFrame and add investor_id if not present
            df = pd.json_normalize(data['Data']['Records'])
            df = pd.DataFrame(df)
            if not df.empty:
                if 'investor_id' not in df.columns:
                    df['investor_id'] = investor_id
                return df
            return pd.DataFrame()
            
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for investor {investor_id}: {str(e)}")
            if attempt < RETRY_COUNT - 1:
                time.sleep(2)  # Wait before retrying
            continue
            
    print(f"All attempts failed for investor {investor_id}")
    return pd.DataFrame()

def process_investor_batch(investor_ids):
    """Process a batch of investor IDs and append results to global DataFrame"""
    batch_data = pd.DataFrame()
    for investor_id in investor_ids:
        investor_data = fetch_single_investor_data(investor_id)
        if not investor_data.empty:
            batch_data = pd.concat([batch_data, investor_data], ignore_index=True)
    
    # Safely append to global DataFrame
    if not batch_data.empty:
        with data_lock:
            global combined_data
            combined_data = pd.concat([combined_data, batch_data], ignore_index=True)

def clean_and_convert_data(df):
    """Clean data and handle data type conversions"""
    if df.empty:
        return df
    
    # Convert date columns
    date_columns = ['initialpurdate', 'navdate']
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Convert numeric columns
    numeric_columns = [
        'investedamt', 'purchaseunits', 'saleunits', 'saleamount', 'balanceunits',
        'avgcost', 'currentnav', 'currentvalue', 'notionalpl', 'bookedpl',
        'dividendpay', 'absretn', 'xirr', 'weightage'
    ]
    
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Clean string columns
    string_columns = [
        'investorcode', 'investorname', 'investorpan', 'foliono', 'schcode',
        'prodcode', 'foliosch', 'amcid', 'amcname', 'schemename', 'category',
        'holding', 'invcode', 'divflag', 'isin', 'dpid'
    ]
    
    for col in string_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    
    return df

def save_to_excel(df, file_path):
    """Save DataFrame to Excel file"""
    if not df.empty:
        df.to_excel(file_path, index=False)
        print(f"Data saved to Excel file: {file_path}")
    else:
        print("No data to save to Excel")

def save_to_sql(df, table_name):
    """Save DataFrame to SQL table"""
    if df.empty:
        print("No data to save to SQL")
        return
    
    engine = create_engine(DB_CONNECTION_STRING)
    
    # Define SQL data types
    dtype_mapping = {
        'investorcode': types.String(length=50),
        'investorname': types.String(length=100),
        'investorpan': types.String(length=20),
        'foliono': types.String(length=50),
        'schcode': types.String(length=20),
        'prodcode': types.String(length=20),
        'foliosch': types.String(length=100),
        'amcid': types.String(length=20),
        'amcname': types.String(length=100),
        'schemename': types.String(length=200),
        'category': types.String(length=50),
        'initialpurdate': types.DateTime(),
        'investedamt': types.Float(),
        'purchaseunits': types.Float(),
        'saleunits': types.Float(),
        'saleamount': types.Float(),
        'balanceunits': types.Float(),
        'avgcost': types.Float(),
        'navdate': types.DateTime(),
        'currentnav': types.Float(),
        'currentvalue': types.Float(),
        'notionalpl': types.Float(),
        'bookedpl': types.Float(),
        'dividendpay': types.Float(),
        'absretn': types.Float(),
        'xirr': types.Float(),
        'holding': types.String(length=20),
        'weightage': types.Float(),
        'invcode': types.String(length=50),
        'investorid': types.Integer(),
        'divflag': types.String(length=1),
        'isin': types.String(length=20),
        'dpid': types.String(length=50),
        'investor_id': types.Integer()
    }
    
    # Filter to only include columns that exist in the DataFrame
    dtype_mapping = {k: v for k, v in dtype_mapping.items() if k in df.columns}
    
    try:
        # Use chunksize for large datasets
        columns_count = len(df.columns)
        optimal_chunksize = max(1, 1000 // columns_count)  # Adjust based on your DB's limits
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
            index=False,
            dtype=dtype_mapping,
            chunksize=optimal_chunksize,
            method='multi'
        )
        print(f"Data successfully inserted into {table_name} table")
    except Exception as e:
        print(f"Error saving to SQL: {str(e)}")

        # try:
        #     print("Attempting fallback to single-row inserts...")
        #     df.to_sql(
        #         name=table_name,
        #         con=engine,
        #         if_exists='append',
        #         index=False,
        #         dtype=dtype_mapping,
        #         chunksize=1,
        #         method=None
        #     )
        #     print("Fallback insert completed successfully")
        # except Exception as fallback_error:
        #     print(f"Fallback insert failed: {str(fallback_error)}")
        #     # Save failed data to CSV for manual inspection
        #     error_file = f"failed_insert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        #     df.to_csv(error_file, index=False)
        #     print(f"Saved failed data to {error_file} for manual inspection")

def main():
    start_time = time.time()
    
    # Step 1: Get all investor IDs
    print("Fetching investor IDs from database...")
    investor_ids = get_investor_ids()
    print(f"Found {len(investor_ids)} investors to process")
    
    # Step 2: Process investors in parallel batches
    print("Starting parallel data fetching...")
    
    # Split investor IDs into batches for threading
    batch_size = 50  # Investors per batch
    batches = [investor_ids[i:i + batch_size] for i in range(0, len(investor_ids), batch_size)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(process_investor_batch, batch) for batch in batches]
        
        # Monitor progress
        completed = 0
        total = len(batches)
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            if completed % 10 == 0 or completed == total:
                print(f"Progress: {completed}/{total} batches completed ({completed/total:.1%})")
    
    # Step 3: Clean and convert data
    print("Cleaning and converting data...")
    cleaned_data = clean_and_convert_data(combined_data)
    
    if cleaned_data.empty:
        print("No data fetched from API")
        return
    
    # Step 4: Save to Excel
    print("Saving to Excel...")
    save_to_excel(cleaned_data, EXCEL_FILE_PATH)
    
    # Step 5: Save to SQL
    print("Saving to SQL database...")
    save_to_sql(cleaned_data, SQL_TABLE_NAME)
    
    # Print summary
    duration = time.time() - start_time
    print(f"\nProcessing completed in {duration:.2f} seconds")
    print(f"Total records processed: {len(cleaned_data)}")
    print(f"Unique investors with data: {cleaned_data['investor_id'].nunique()}")

if __name__ == "__main__":
    main()
# Hierarchy Table
import requests
import json
import pandas as pd
from sqlalchemy import create_engine, types, text
from datetime import datetime
import pytz
import concurrent.futures
from threading import Lock
import time


server = '192.168.100.55'
database = 'WEALTHONE'
username = 'aruhat'
password = 'aruhat'
# engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

# API setup
API_URL = "https://mf.kunvarjiwealth.com/fcapi/investor/hierarchy"
# Configuration
AUTH_TOKEN = f"Bearer {generate_token}"
DB_CONNECTION_STRING = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"  # e.g., "mysql+pymysql://user:password@host/db"
EXCEL_FILE_PATH = "HIERARCHY_.xlsx"
# Configuration

with engine.begin() as conn:
    conn.execute(text("DELETE FROM EMPLOYEE_HIERARCHY"))
    
SQL_TABLE_NAME = "EMPLOYEE_HIERARCHY"
MAX_THREADS = 20  # Adjust based on your API rate limits
REQUEST_TIMEOUT = 30  # seconds
RETRY_COUNT = 3  # Number of retries for failed requests

# Headers for API request
headers = {
    'Content-Type': 'application/json',
    'Authorization': AUTH_TOKEN,
    'Cookie': 'ARRAffinity=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47; ARRAffinitySameSite=4e8ccd4f67b1da5ef34b65dbf931b58eed34c4c0959021149790d2b0159c4b47'
}

# Global variables for thread-safe operations
data_lock = Lock()
combined_data = pd.DataFrame()

def get_investor_ids():
    """Fetch investor IDs from investor_master table"""
    engine = create_engine(DB_CONNECTION_STRING)
    query = "SELECT DISTINCT Id FROM investor_master"
    df = pd.read_sql(query, engine)
    return df['Id'].tolist()

def fetch_single_investor_data(investor_id):
    """Fetch data from API for a single investor with retry logic"""
    as_on_date = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    payload = json.dumps({
        "InvestorId": investor_id,
        "RefKey": "string"
    })
    
    for attempt in range(RETRY_COUNT):
        try:
            response = requests.post(
                API_URL,
                headers=headers,
                data=payload,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            data = response.json()
            
            # Convert to DataFrame and add investor_id if not present
            df = pd.json_normalize(data['Data']['RmInfo'])
            df = pd.DataFrame(df)
            if not df.empty:
                if 'investor_id' not in df.columns:
                    df['investor_id'] = investor_id
                return df
            return pd.DataFrame()
            
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed for investor {investor_id}: {str(e)}")
            if attempt < RETRY_COUNT - 1:
                time.sleep(2)  # Wait before retrying
            continue
            
    print(f"All attempts failed for investor {investor_id}")
    return pd.DataFrame()

def process_investor_batch(investor_ids):
    """Process a batch of investor IDs and append results to global DataFrame"""
    batch_data = pd.DataFrame()
    for investor_id in investor_ids:
        investor_data = fetch_single_investor_data(investor_id)
        if not investor_data.empty:
            batch_data = pd.concat([batch_data, investor_data], ignore_index=True)
    
    # Safely append to global DataFrame
    if not batch_data.empty:
        with data_lock:
            global combined_data
            combined_data = pd.concat([combined_data, batch_data], ignore_index=True)

def clean_and_convert_data(df):
    """Clean data and handle data type conversions"""
    if df.empty:
        return df
    
    # Convert date columns
    date_columns = []
    for col in date_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Convert numeric columns
    numeric_columns = [
        'EmpID', 'PinCode', 'Mobile'
    ]
    
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Clean string columns
    string_columns = [
        'EmpCode', 'EmployeeName', 'Address1', 'Address2', 'Address3',
        'City', 'State', 'Country', 'PhoneNo', 'Email'
    ]
    
    for col in string_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    
    return df

def save_to_excel(df, file_path):
    """Save DataFrame to Excel file"""
    if not df.empty:
        df.to_excel(file_path, index=False)
        print(f"Data saved to Excel file: {file_path}")
    else:
        print("No data to save to Excel")

def save_to_sql(df, table_name):
    """Save DataFrame to SQL table"""
    if df.empty:
        print("No data to save to SQL")
        return
    
    engine = create_engine(DB_CONNECTION_STRING)
    
    # Define SQL data types
    dtype_mapping = {
        'EmpID': types.Integer(),
        'EmpCode': types.String(length=50),
        'EmployeeName': types.String(length=255),
        'Address1': types.String(length=255),
        'Address2': types.String(length=255),
        'Address3': types.String(length=255),
        'City': types.String(length=100),
        'State': types.String(length=100),
        'PinCode': types.Integer(),
        'Country': types.String(length=200),
        'Mobile': types.String(length=200),
        'PhoneNo': types.String(length=150),
        'Email': types.String(length=200),
      
    }
    
    # Filter to only include columns that exist in the DataFrame
    dtype_mapping = {k: v for k, v in dtype_mapping.items() if k in df.columns}
    
    try:
        # Use chunksize for large datasets
        columns_count = len(df.columns)
        optimal_chunksize = max(1, 1000 // columns_count)  # Adjust based on your DB's limits
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
            index=False,
            dtype=dtype_mapping,
            chunksize=optimal_chunksize,
            method='multi'
        )
        print(f"Data successfully inserted into {table_name} table")
    except Exception as e:
        print(f"Error saving to SQL: {str(e)}")

        # try:
        #     print("Attempting fallback to single-row inserts...")
        #     df.to_sql(
        #         name=table_name,
        #         con=engine,
        #         if_exists='append',
        #         index=False,
        #         dtype=dtype_mapping,
        #         chunksize=1,
        #         method=None
        #     )
        #     print("Fallback insert completed successfully")
        # except Exception as fallback_error:
        #     print(f"Fallback insert failed: {str(fallback_error)}")
        #     # Save failed data to CSV for manual inspection
        #     error_file = f"failed_insert_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        #     df.to_csv(error_file, index=False)
        #     print(f"Saved failed data to {error_file} for manual inspection")

def main():
    start_time = time.time()
    
    # Step 1: Get all investor IDs
    print("Fetching investor IDs from database...")
    investor_ids = get_investor_ids()
    print(f"Found {len(investor_ids)} investors to process")
    
    # Step 2: Process investors in parallel batches
    print("Starting parallel data fetching...")
    
    # Split investor IDs into batches for threading
    batch_size = 50  # Investors per batch
    batches = [investor_ids[i:i + batch_size] for i in range(0, len(investor_ids), batch_size)]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        futures = [executor.submit(process_investor_batch, batch) for batch in batches]
        
        # Monitor progress
        completed = 0
        total = len(batches)
        for future in concurrent.futures.as_completed(futures):
            completed += 1
            if completed % 10 == 0 or completed == total:
                print(f"Progress: {completed}/{total} batches completed ({completed/total:.1%})")
    
    # Step 3: Clean and convert data
    print("Cleaning and converting data...")
    cleaned_data = clean_and_convert_data(combined_data)
    
    if cleaned_data.empty:
        print("No data fetched from API")
        return
    
    # Step 4: Save to Excel
    print("Saving to Excel...")
    save_to_excel(cleaned_data, EXCEL_FILE_PATH)
    
    # Step 5: Save to SQL
    print("Saving to SQL database...")
    save_to_sql(cleaned_data, SQL_TABLE_NAME)
    
    # Print summary
    duration = time.time() - start_time
    print(f"\nProcessing completed in {duration:.2f} seconds")
    print(f"Total records processed: {len(cleaned_data)}")
    print(f"Unique investors with data: {cleaned_data['investor_id'].nunique()}")

if __name__ == "__main__":
    main()
# /fcapi/reports/mf/collection-report
%history -f MF_DATA_FETCHING.py
