# https://leetcode.com/problems/validate-ip-address/

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.ipv4(IP):
            return "IPv4"
        if self.ipv6(IP):
            return "IPv6"
        return "Neither"


    def ipv4(self, IP: str) -> bool:
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if len(part) > 1 and part[0] == '0':
                return False
            try:
                part = int(part)
                if part < 0 or part > 255:
                    return False
            except:
                return False
        return True

    def ipv6(self, IP: str) -> bool:
        parts = IP.split(":")
        if len(parts) != 8:
            return False
        for part in parts:
            if len(part) < 1 or len(part) > 4:
                return False
            try:
                int(part, 16)
            except:
                return False
        return True


# print(Solution().validIPAddress("172.16.254.1"))
print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print(Solution().validIPAddress("256.256.256.256"))
# print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
# print(Solution().validIPAddress("1e1.4.5.6"))
