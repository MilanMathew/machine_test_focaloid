def check_ip_address(address):
    """
    Returns whether a string is a valid Ipv4 or Ipv6 address or neither.

        Parameters:
            address (str): address string

        Returns:
            address type (str): IPv4, IPv6 or Neither

    >>> check_ip_address('')                                          # empty string  
    'Neither'
    >>> check_ip_address('172.16.254.1')
    'IPv4'
    >>> check_ip_address('256.256.256.256')                           # out of the range 0-255  
    'Neither'
    >>> check_ip_address('2001:0db8:85a3::8a2e:0370:7334')            # double colon
    'IPv6'
    >>> check_ip_address('2001:db8:85a3:0:0:8A2E:0370:7334')          # uppercase
    'IPv6'
    >>> check_ip_address('02001:0db8:85a3:0000:0000:8a2e:0370:7334')  # extra leading zero
    'Neither'
    """
    from ipaddress import ip_address

    try:
        ip = ip_address(address)
        return repr(ip)[:4]
    except ValueError:
        return "Neither"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
