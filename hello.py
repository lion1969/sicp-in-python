from urllib.request import urlopen

shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
# words = set(shakespeare.read().decode().split())


# assert isinstance(shakespeare, http.client.HTTPResponse)
print(shakespeare.read().decode())
