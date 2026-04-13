from flask import Flask
import requests
from frontend import generate_html

app = Flask(__name__)

# Base URL of your server.py APIs
BASE_URL = "http://127.0.0.1:5000/api"

@app.route('/')
def home():
    try:
        # 1. Connect to the server.py API to get all names
        names_response = requests.get(f"{BASE_URL}/names")
        names_response.raise_for_status() # Raise an exception for HTTP errors
        
        names = names_response.json()
        
        profiles_data = []
        # 2. Iterate through each name to fetch their specific role and hobby iteratively
        for name in names:
            role_res = requests.get(f"{BASE_URL}/roles/{name}")
            hobby_res = requests.get(f"{BASE_URL}/hobbies/{name}")
            
            role = role_res.json().get("role", "Unknown") if role_res.status_code == 200 else "Unknown"
            hobby = hobby_res.json().get("hobby", "Unknown") if hobby_res.status_code == 200 else "Unknown"
            
            profiles_data.append({
                "profile_name": name,
                "profile_image": role,
                "profile_bio": hobby
            })
            
        # 3. Use the imported function from frontend.py to build the UI
        html_content = generate_html(profiles_data)
        
        return html_content
    except requests.exceptions.RequestException as e:
        # Fallback if the server fails to connect
        return f"""
        <div style="font-family: sans-serif; padding: 40px; text-align: center;">
            <h1 style="color: #ef4444;">Error Connecting to Backend!</h1>
            <p>Make sure you have <strong>server.py</strong> running in another terminal window first.</p>
            <code style="background: #eee; padding: 10px; display: inline-block; margin-top: 10px;">{e}</code>
        </div>
        """

if __name__ == '__main__':
    print("Starting client UI server on port 5001...")
    # Run the client server on port 5001, completely separate from the backend server
    app.run(port=5001, debug=True)
