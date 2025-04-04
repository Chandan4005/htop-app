from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import getpass
import datetime
import pytz
import subprocess

def htop(request):
    name = "Chandan S Rathod"  # 👈 Replace with your actual full name
    try:
        username = getpass.getuser()  # More reliable than os.getlogin()
    except Exception as e:
        username = f"Error: {str(e)}"

    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get 'top' command output
    try:
        top_output = subprocess.getoutput("top -b -n 1 | head -20")
    except Exception as e:
        top_output = f"Error running top: {str(e)}"

    html = f"""
    <h1>System Info</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>user:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <p><b>TOP output:</b></p>
    <pre>{top_output}</pre>
    """
    return HttpResponse(html)
