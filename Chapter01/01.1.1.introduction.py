import http.client
from urllib.request import urlopen

shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')

assert isinstance(shakespeare, http.client.HTTPResponse)
words = set(shakespeare.read().decode().split())
print(words)
exit(0)
print({w for w in words if len(w) >= 4 and w[::-1] in words})
# print({w for w in words if len(w) >= 5 and w[::-1] in words and w[::-1] == 'speed'})
print("fdsfas")
