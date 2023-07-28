import hashlib

'''Build a URL shortener service that converts long URLs 
into shorter, more manageable ones. The project will use 
a simple hash function to generate short codes for the 
original URLs, and it will maintain a mapping of short 
codes to the original URLs.'''

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        short_code = self._generate_short_code(original_url)
        self.url_mapping[short_code] = original_url
        return short_code

    def _generate_short_code(self, original_url):
        # Use MD5 hash as a simple way to generate a short code
        hash_object = hashlib.md5(original_url.encode())
        return hash_object.hexdigest()[:8]

    def get_original_url(self, short_code):
        return self.url_mapping.get(short_code, "URL not found.")

# Usage example
shortener = URLShortener()
short_code = shortener.shorten_url("https://www.example.com/some/long/url")
print("Shortened URL:", short_code)
print("Original URL:", shortener.get_original_url(short_code))