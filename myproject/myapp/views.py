from django.http import HttpResponse
import os
import time
import psutil
from datetime import datetime
import pytz

def htop(request):
    name = "K Adarsha Nayaka" 
    username = os.getenv("USER")  

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    top_output = "\n".join([f"PID: {p.info['pid']}, Name: {p.info['name']}, User: {p.info['username']}" 
                            for p in psutil.process_iter(['pid', 'name', 'username'])])

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
