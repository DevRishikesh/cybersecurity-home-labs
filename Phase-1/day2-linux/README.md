# Day 2 – Linux Security Hardening

## Objective
Harden a Linux system by reducing privileges and securing SSH access.

## Security Measures Implemented
- Created a low-privilege user
- Disabled root SSH login
- Disabled password authentication
- Changed SSH port

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

## SSH Brute Force Experiment (Learning Exercise)

As part of understanding SSH security from both attacker and defender perspectives, I intentionally created a vulnerable scenario in a controlled lab environment.

### What I Did
- Created a new low-privilege user with a weak password (`123456`)
- Enabled password-based SSH authentication
- Used Hydra to perform a brute force attack against the SSH service
- Successfully authenticated after repeated login attempts

### Defender’s Perspective
- Monitored SSH authentication logs using `/var/log/auth.log`
- Observed multiple failed login attempts followed by a successful login
- Identified clear indicators of a brute force attack from log entries

### Key Takeaways
- Weak passwords make SSH services extremely vulnerable
- Password-based authentication is unsafe for exposed services
- Authentication logs are critical for detecting brute force attacks
- Proper SSH hardening and monitoring are essential for system security

> **Note:** This experiment was performed only on my own lab system for educational purposes.

## Screenshots

![screenshot](img1.png)

![screenshot](img2.png)

![screenshot](img3.png)

![screenshot](img4.png)
