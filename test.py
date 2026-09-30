import os
import requests
from dotenv import load_dotenv

# 1. Load the variables from your .env file
load_dotenv()

# 2. Grab your key (Make sure the name matches what is inside your .env)
API_KEY = os.getenv("YOUR-API-KEY") 

if not API_KEY:
    print("❌ Error: Could not find the API key in your .env file. Check the variable name!")
else:
    # 3. Construct the official Pair endpoint URL
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/INR/NGN"
    
    print(f"Sending request to ExchangeRate-API...")
    response = requests.get(url)
    
    # 4. Check the result
    if response.status_code == 200:
        data = response.json()
        if data.get("result") == "success":
            print("✅ API is working perfectly!")
            print(f"1 INR = {data.get('conversion_rate')} NGN")
        else:
            print(f"❌ API returned an error status: {data}")
    else:
        print(f"❌ HTTP Error {response.status_code}: Something is wrong with the request.")
        print(response.text)
