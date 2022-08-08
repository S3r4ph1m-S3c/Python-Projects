import dns.resolver
def A(domain):
    result = dns.resolver.query(domain, 'A')
    for val in result:
        print('A Record : ', val.to_text())