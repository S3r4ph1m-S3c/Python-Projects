import dns.resolver
def AAAA(domain):
    result = dns.resolver.query(domain, 'AAAA')
    for val in result:
        print('AAAA Record : ', val.to_text())
