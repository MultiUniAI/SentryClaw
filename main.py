from sentry.engine import SentryProxy
def main():
  s = SentryProxy()
  print(f"Result: {s.inspect("http://test.com", "email@roy.com", "http")}")
if __name__ == "__main__": main()