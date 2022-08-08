import dns.resolver
def TXT(domain):
    result = dns.resolver.query(domain, 'TXT')
    for val in result:
        print('TXT Record : ', val.to_text())