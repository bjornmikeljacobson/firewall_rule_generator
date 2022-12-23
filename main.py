import re


def generate_firewall_rule(protocol, port, action, description):
    # Validate the protocol
    if protocol not in ["tcp", "udp"]:
        raise ValueError("Invalid protocol")

    # Validate the port
    if not re.match(r'\d+', port):
        raise ValueError("Invalid port")
    port = int(port)
    if port < 1 or port > 65535:
        raise ValueError("Invalid port")

    # Validate the action
    if action not in ["allow", "block"]:
        raise ValueError("Invalid action")

    # Generate the firewall rule
    new_rule = f"{action} {protocol} {port} {description}"
    return new_rule


# Test the firewall rule generator
rule = generate_firewall_rule("tcp", "80", "allow", "HTTP traffic")
print(rule)
