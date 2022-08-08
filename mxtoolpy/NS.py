import dns.resolver


def NS(domain):
    result = dns.resolver.query(domain, 'NS')
    for val in result:
        print('NS Record : ', val.to_text())
