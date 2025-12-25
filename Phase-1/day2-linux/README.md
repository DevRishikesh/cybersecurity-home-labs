# Day 2 – Linux Security Hardening

## Objective
Harden a Linux system by reducing privileges and securing SSH access.

## Security Measures Implemented
- Created a low-privilege user
- Disabled root SSH login
- Disabled password authentication
- Changed SSH port
- Implemented key-based authentication
- Disabled unnecessary services

## What I Learned
- Why least privilege is critical
- How SSH is a common attack vector
- How defenders reduce attack surface

## Issue Faced & Resolution
While backing up SSH configuration, I initially tried copying a directory without using the recursive flag.

Error:
cp: -r not specified; omitting directory

Resolution:
Used the `-r` flag to copy the directory recursively.

Lesson:
Linux treats files and directories differently. Backups of security configs must be done carefully to avoid misconfiguration or lockout.


## Screenshots
(Add screenshots)
