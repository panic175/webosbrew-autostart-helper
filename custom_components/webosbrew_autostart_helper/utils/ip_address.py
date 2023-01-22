"""IP address"""
import ipaddress


def is_ip_valid(ip: str) -> bool:
    """Checks if given IP is a valid one"""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
