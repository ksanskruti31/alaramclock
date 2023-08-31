import random

def shorten_url(long_url):
  short_url = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(6))
  return short_url

def main():
  long_url = 'https://www.google.com'
  short_url = shorten_url(long_url)
  print('The shortened URL is:', short_url)

if __name__ == '__main__':
  main() 
