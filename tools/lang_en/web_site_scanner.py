import socket
import concurrent.futures
import requests
from urllib.parse import urlparse
import ssl
import time
import re
import dns.resolver
from bs4 import BeautifulSoup
import whois
from colorama import Fore, Style, init
from rich.console import Console
from requests.exceptions import RequestException

def print_with_delay(text, delay=0.05):
    lines = text.splitlines()
    for line in lines:
        print(Fore.LIGHTBLUE_EX + line)
        time.sleep(delay)

banner = """
██╗    ██╗███████╗██████╗ ███████╗██╗████████╗███████╗
██║    ██║██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝██╔════╝
██║ █╗ ██║█████╗  ██████╔╝███████╗██║   ██║   █████╗  
██║███╗██║██╔══╝  ██╔══██╗╚════██║██║   ██║   ██╔══╝  
╚███╔███╔╝███████╗██████╔╝███████║██║   ██║   ███████╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚══════╝
                                                      
"""

init(autoreset=True)

console = Console()


ENABLE_COLORS = False  

def current_time_hour():
    return time.strftime("%H:%M:%S")

def log(category, message, data, color=Fore.WHITE):
    if ENABLE_COLORS:
        console.print(f"{current_time_hour()} [{category}] {message}: {color}{data}{Style.RESET_ALL}")
    else:
        console.print(f"{current_time_hour()} [{category}] {message}: {data}")

# --- Category: General Information ---
def website_found_url(url):
    if not urlparse(url).scheme:
        website_url = "https://" + url
    else:
        website_url = url
    log("General Info", "Website", website_url, Fore.CYAN)
    return website_url

def website_domain(website_url):
    domain = urlparse(website_url).netloc
    log("General Info", "Domain", domain, Fore.GREEN)
    return domain

def website_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        log("General Info", "IP", ip, Fore.YELLOW)
    except socket.gaierror:
        ip = None
        log("General Info", "IP", "None", Fore.RED)
    return ip

def ip_type(ip):
    if ip is None:
        return
    ip_type = "ipv6" if ':' in ip else "ipv4" if '.' in ip else "Unknown"
    log("General Info", "IP Type", ip_type, Fore.MAGENTA)

# --- Category: Performance ---
def test_performance(website_url):
    try:
        start_time = time.time()
        response = requests.get(website_url, timeout=10)
        end_time = time.time()
        response_time = end_time - start_time
        log("Performance", "Response Time", f"{response_time:.2f} seconds", Fore.CYAN)
        log("Performance", "Response Size", f"{len(response.content)} bytes", Fore.CYAN)
    except RequestException:
        log("Performance", "Error", "Unable to measure performance", Fore.RED)

def website_status(website_url):
    try:
        response = requests.get(website_url, timeout=5)
        log("Performance", "Status Code", response.status_code, Fore.GREEN if response.status_code == 200 else Fore.RED)
    except RequestException:
        log("Performance", "Status Code", "404", Fore.RED)

# --- Category: Security ---
def website_secure(website_url):
    secure = website_url.startswith("https://")
    log("Security", "Secure (HTTPS)", secure, Fore.BLUE)

def check_ssl_certificate(website_url):
    try:
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=urlparse(website_url).hostname) as sock:
            sock.settimeout(5)
            sock.connect((urlparse(website_url).hostname, 443))
            cert = sock.getpeercert()
            for key, value in cert.items():
                log("Security", f"SSL Certificate {key}", value, Fore.CYAN)
    except:
        log("Security", "SSL Certificate", "Unable to retrieve", Fore.RED)

def check_security_headers(website_url):
    headers_of_interest = ['Content-Security-Policy', 'Strict-Transport-Security', 'X-Content-Type-Options', 'X-Frame-Options', 'X-XSS-Protection']
    try:
        response = requests.get(website_url, timeout=5)
        for header in headers_of_interest:
            log("Security", f"Security Header {header}", response.headers.get(header, "Missing"), Fore.YELLOW)
    except RequestException:
        log("Security", "Headers", "Error retrieving headers", Fore.RED)

def analyze_cookies(website_url):
    try:
        response = requests.get(website_url, timeout=5)
        for cookie in response.cookies:
            secure = 'Secure' if cookie.secure else 'Not Secure'
            httponly = 'HttpOnly' if cookie.has_nonstandard_attr('HttpOnly') else 'Not HttpOnly'
            log("Security", f"Cookie {cookie.name}", f"{secure}, {httponly}", Fore.BLUE)
    except RequestException:
        log("Security", "Cookies", "Unable to retrieve cookies", Fore.RED)

def check_redirections(website_url):
    try:
        response = requests.get(website_url, timeout=5, allow_redirects=True)
        if response.history:
            for resp in response.history:
                log("Security", f"Redirection {resp.url}", f"Status {resp.status_code}", Fore.YELLOW)
            log("Security", f"Final URL {response.url}", f"Status {response.status_code}", Fore.GREEN)
    except RequestException:
        log("Security", "Redirections", "Error retrieving redirections", Fore.RED)

# --- Category: Network Information ---
def ip_info(ip):
    api_url = f"https://ipinfo.io/{ip}/json"
    try:
        response = requests.get(api_url)
        data = response.json()
        for key, label in [('country', 'Host Country'), ('hostname', 'Host Name'), ('org', 'Host Org'), ('asn', 'Host AS')]:
            value = data.get(key, 'None')
            if value != 'None':
                log("Network", label, value, Fore.CYAN)
    except RequestException:
        log("Network", "IP Info", "Unable to retrieve IP info", Fore.RED)

def ip_dns(ip):
    try:
        dns_name, _, _ = socket.gethostbyaddr(ip)
        log("Network", "Host DNS", dns_name, Fore.YELLOW)
    except socket.herror:
        log("Network", "Host DNS", "None", Fore.RED)

def website_port(ip):
    ports = {
        21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS", 69: "TFTP",
        80: "HTTP", 110: "POP3", 443: "HTTPS", 3306: "MySQL", 5432: "PostgreSQL"
    }

    def scan_port(ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    log("Network", f"Port {port}", f"Open ({ports.get(port, 'Unknown')})", Fore.GREEN)
        except:
            pass

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

def analyze_dns(domain):
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        for ip in a_records:
            log("Network", "DNS A Record", ip.to_text(), Fore.YELLOW)

        mx_records = dns.resolver.resolve(domain, 'MX')
        for record in mx_records:
            log("Network", "DNS MX Record", record.exchange.to_text(), Fore.YELLOW)

        txt_records = dns.resolver.resolve(domain, 'TXT')
        for txt in txt_records:
            log("Network", "DNS TXT Record", txt.to_text(), Fore.YELLOW)
    except:
        log("Network", "DNS", "Error retrieving DNS records", Fore.RED)

# --- Category: Technologies ---
def detect_technologies(website_url):
    try:
        response = requests.get(website_url, timeout=5)
        headers = response.headers
        technologies = []

        if 'x-powered-by' in headers:
            technologies.append(f"X-Powered-By: {headers['x-powered-by']}")
        if 'server' in headers:
            technologies.append(f"Server: {headers['server']}")

        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup.find_all('script', src=True):
            if 'jquery' in script['src']:
                technologies.append("jQuery")
            if 'bootstrap' in script['src']:
                technologies.append("Bootstrap")

        if technologies:
            for tech in technologies:
                log("Technologies", "Detected Technology", tech, Fore.MAGENTA)
        else:
            log("Technologies", "Detected Technology", "No specific technologies detected", Fore.RED)
    except RequestException:
        log("Technologies", "Error", "Unable to detect technologies", Fore.RED)

# --- Category: WHOIS ---
def analyze_whois(domain):
    try:
        whois_info = whois.whois(domain)
        if whois_info:
            log("WHOIS", "Registrar", whois_info.registrar, Fore.CYAN)
            log("WHOIS", "Creation Date", whois_info.creation_date, Fore.CYAN)
            log("WHOIS", "Expiration Date", whois_info.expiration_date, Fore.CYAN)
            log("WHOIS", "Name Servers", ', '.join(whois_info.name_servers), Fore.CYAN)
    except:
        log("WHOIS", "Error", "Unable to retrieve WHOIS info", Fore.RED)

try:

    print_with_delay(Fore.LIGHTBLUE_EX + banner, delay=0.05)
    print()
    url = input(Fore.LIGHTWHITE_EX + f"[Exalty] Website URL -> ")
    website_url = website_found_url(url)
    domain = website_domain(website_url)
    ip = website_ip(domain)
    ip_type(ip)
    
    test_performance(website_url)
    website_status(website_url)
    
    website_secure(website_url)
    check_ssl_certificate(website_url)
    check_security_headers(website_url)
    analyze_cookies(website_url)
    check_redirections(website_url)
    
    ip_info(ip)
    ip_dns(ip)
    analyze_dns(domain)
    website_port(ip)

    detect_technologies(website_url)

    analyze_whois(domain)

except Exception as e:
    log("Error", f"An error occurred: {e}", Fore.RED)
