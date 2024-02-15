"""535. Encode and Decode TinyURL"""

import base64


class Codec:
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        return str(
            base64.urlsafe_b64encode(bytes(longUrl, encoding="utf8")), encoding="utf8"
        )

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return str(base64.urlsafe_b64decode(shortUrl), encoding="utf8")


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
