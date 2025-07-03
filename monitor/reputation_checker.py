import requests

def check_ip(ip, api_key):
    url = "https://api.abuseipdb.com/api/v2/check"
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    headers = {"Key": api_key, "Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["abuseConfidenceScore"]
        else:
            return 0
    except Exception as e:
        print(f"[!] Reputation check failed: {e}")
        return 0
