# https://leetcode.com/problems/encode-and-decode-tinyurl/

# https://youtu.be/VyBOaboQLGc
import random
import string

class Codec:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        self.encodeMap = {}
        self.decodeMap = {}

    def getShortUrl(self):
        code = ''.join(random.choice(self.chars) for _ in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        if longUrl in self.encodeMap:
            return self.encodeMap[longUrl]
        
        shortUrl = self.getShortUrl()
        # Ensure unique shortUrl
        while shortUrl in self.decodeMap:
            shortUrl = self.getShortUrl()
        
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]


# ================= DRIVER CODE =================
if __name__ == "__main__":
    codec = Codec()
    
    url1 = "https://www.example.com/page1"
    url2 = "https://www.example.com/page2"
    
    short1 = codec.encode(url1)
    short2 = codec.encode(url2)
    
    print("Original URL:", url1, "→ Short URL:", short1)
    print("Original URL:", url2, "→ Short URL:", short2)
    
    print("Decoded URL from short1:", codec.decode(short1))
    print("Decoded URL from short2:", codec.decode(short2))


# Time: O(1)
# Space: O(N) ; where N is number of longUrl
    
    
import string
class Codec:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        # self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.encodeMap = {}
        self.decodeMap = {}
    
    def getShortUrl(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code
        
    def encode(self, longUrl: str) -> str:
        shortUrl = self.getShortUrl()
        while shortUrl in self.encodeMap:
            shortUrl = self.encodeMap()
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
    
    

    