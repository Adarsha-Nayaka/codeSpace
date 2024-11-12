from django.http import HttpResponse
import os
import time
import psutil
from datetime import datetime

def htop(request):
    # Name and system username
    name = "K Adarsha Nayaka"  # Replace with your full name
    username = os.getenv("USER")  # System username (Unix-based systems)

    # Get current server time in IST (Indian Standard Time)
    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate top output (list of processes)
    top_output = "\n".join([f"PID: {p.info['pid']}, Name: {p.info['name']}, User: {p.info['username']}" 
                            for p in psutil.process_iter(['pid', 'name', 'username'])])

    # Prepare the HTML response
    response_content = f"""
    <html>
    <body>
    <h1>System Information</h1>
    <p>Name: {name}</p>
    <p>Username: {username}</p>
    <p>Server Time (IST): {server_time}</p>
    <h2>Top Output:</h2>
    <pre>{top_output}</pre>
    </body>
    </html>
    """
    return HttpResponse(response_content)
