import dns.resolver
import os
import argparse
from colorama import Fore, Style

def resolve_cname(domain):
    try:
        result = dns.resolver.resolve(domain, 'CNAME')
        return result[0].target.to_text()
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"{Fore.YELLOW}No CNAME record found for {domain}.")
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
            print(f"{Fore.GREEN}{cname_target} is dangling (no valid IP address).")
        else:
            print(f"{Fore.WHITE}{cname_target} resolves successfully.")
    else:
        print(f"{domain} does not have a CNAME record.")

def check_domains_from_file(file_path):
    if not os.path.isfile(file_path):
        print(f"File {file_path} not found.")
        return
    with open(file_path, 'r') as file:
        domains = file.readlines()
        for domain in domains:
            domain = domain.strip()
            if domain:
                print(f"{Fore.RED}Checking {domain}...")
                check_dangling_cname(domain)


def main():
    parser = argparse.ArgumentParser(description="Check CNAME Dangling Issues")
    parser.add_argument('-d','--domain', type=str, help="Check single domain")
    parser.add_argument('-l','--list', type=str, help="File containing list of domains")

    args = parser.parse_args()
    if args.domain:
        print(f"Checking single domain: {args.domain}")
        check_dangling_cname(args.domain)
    elif args.list:
        print(f"Checking list of domains: {args.list}")
        check_domains_from_file(args.list)
    else:
        print("You must provide either a domain or list of domains.")
    

if __name__ == "__main__":
    main()
