import dns.resolver
def CNAME(domain):
      try:
        result = dns.resolver.query(domain, 'CNAME')
        for val in result:
            print('CNAME Record : ', val.target)
      except:
          print("[***] CNAME don't could be detected...")
