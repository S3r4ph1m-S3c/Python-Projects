import dns.resolver
def MX(domain):
    result = dns.resolver.query(domain, 'MX')
    for val in result:
        print('MX Record : ', val.to_text())