#!/bin/bash
# Simple Endpoint Security Baseline Auditor

# Check if root login is disabled
echo "Checking if root login is disabled..."
grep "PermitRootLogin" /etc/ssh/sshd_config || echo "Root login is not disabled."

# Check for world-writable files
echo "Checking for world-writable files..."
find / -type f -perm -0002 2>/dev/null || echo "No world-writable files found."

# Check for sudo misuse
echo "Checking for unnecessary sudo privileges..."
grep -v '^#' /etc/sudoers

# Check kernel parameters (e.g., disable core dumps)
echo "Checking kernel parameters..."
sysctl -a | grep core_pattern

# Check system logs for failed login attempts
echo "Checking system logs for failed login attempts..."
grep "Failed password" /var/log/auth.log
