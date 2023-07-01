def defang(ip : str) -> str:
    # return ip.replace(".", "[.]")

    ans = ''
    for ch in ip:
        if ch == ".":
            ans += "[.]"
        else:
            ans += #ch
    return ans


testip = "192.168.22.22"

print(defang(testip))