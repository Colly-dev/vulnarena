"""
⚠️ INTENTIONALLY VULNERABLE LAB ENGINE ⚠️
Description: Main orchestration engine for the VulnArena lab.
"""

import click
import subprocess
import os

@click.group()
def main():
    """VulnArena CLI - Manage your pentest lab environment."""
    pass

@main.command()
def start():
    """Start the lab environment."""
    click.echo("[*] Starting VulnArena Docker containers...")
    subprocess.run(["docker-compose", "up", "-d"])
    click.echo("[+] Lab is running at http://localhost:5000")

@main.command()
def stop():
    """Stop the lab environment."""
    click.echo("[*] Stopping VulnArena Docker containers...")
    subprocess.run(["docker-compose", "down"])
    click.echo("[+] Lab stopped.")

if __name__ == "__main__":
    main()
