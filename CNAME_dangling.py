import dns.resolver

def resolve_cname(domain):
    try:
        result = dns.resolver.resolve(domain, 'CNAME')
        return result[0].target.to_text()
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"No CNAME record found for {domain}.")
        return None
    except Exception as e:
        print(f"Error resolving CNAME for {domain}: {e}")
        return None

def resolve_ip(domain):
    try:

        result = dns.resolver.resolve(domain, 'A')
        return True 
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"{domain} does not resolve to an IP address.")
        return False
    except Exception as e:
        print(f"Error resolving IP for {domain}: {e}")
        return False

def check_dangling_cname(domain):
    cname_target = resolve_cname(domain)
    
    if cname_target:
        print(f"The CNAME for {domain} points to {cname_target}.")
        if not resolve_ip(cname_target):
            print(f"{cname_target} is dangling (no valid IP address).")
        else:
            print(f"{cname_target} resolves successfully.")
    else:
        print(f"{domain} does not have a CNAME record.")


domain = input("Enter a domain to check for dangling CNAME: ")
check_dangling_cname(domain)
