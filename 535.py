# https://leetcode.com/problems/encode-and-decode-tinyurl/


class Codec:
    def __init__(self):
        self.now = 0
        self.d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.d[self.now] = longUrl
        short = str(self.now)
        self.now += 1
        return short


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[int(shortUrl)]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))