"""Module provides function ping a host"""
from subprocess import call, DEVNULL


def ping(ip: str, retries: int) -> int:
    """Ping the given IP x times."""
    return call(["ping", "-c", str(retries), ip], stdout=DEVNULL)


def is_available(ip: str) -> bool:
    """Ping the given IP 3 times to check if it is available."""
    return ping(ip, 3) == 0
