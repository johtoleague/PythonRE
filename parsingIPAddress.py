import re

def extract_unique_ips(text):
    # Wrap the whole IP pattern in one group
    pattern = r"\b((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))\b"
    ips = re.findall(pattern, text)
   
    unique_ips = list(set(ips))
    return unique_ips

# Test the function
text = "There are some IPs: 192.168.0.1, 127.0.0.1, 192.168.0.1, 255.255.255.0 192.168.0.1, 127.0.0.1, 192.168.0.1, 255.255.255."
print(extract_unique_ips(text))