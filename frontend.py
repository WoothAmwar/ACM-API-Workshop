def generate_html(profiles):
    """
    Generates an HTML string dynamically based on the profiles list provided.
    """
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ACM API Demo Profiles</title>
        <style>
            :root {
                --primary: #2563eb;
                --bg: #f8fafc;
                --card-bg: #ffffff;
                --text-main: #1e293b;
                --text-muted: #64748b;
            }
            body { 
                font-family: 'Inter', system-ui, sans-serif; 
                background-color: var(--bg); 
                padding: 40px 20px; 
                margin: 0;
            }
            .header-title {
                text-align: center;
                color: var(--text-main);
                font-size: 2.5rem;
                margin-bottom: 40px;
                font-weight: 700;
                letter-spacing: -0.025em;
            }
            .container { 
                display: flex; 
                flex-wrap: wrap; 
                gap: 30px; 
                justify-content: center; 
                max-width: 1200px;
                margin: 0 auto;
            }
            .card { 
                background: var(--card-bg); 
                padding: 30px; 
                border-radius: 16px; 
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1); 
                width: 280px; 
                text-align: center; 
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
            }
            .role-badge {
                background: #e2e8f0;
                color: #0f172a;
                padding: 6px 12px;
                border-radius: 999px;
                font-size: 0.75rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                display: inline-block;
                margin-bottom: 20px;
            }
            .card h2 { 
                color: var(--text-main); 
                margin: 0 0 10px 0;
                font-size: 1.5rem;
            }
            .card p { 
                color: var(--text-muted); 
                margin: 0;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <h1 class="header-title">ACM Board Profiles (via API)</h1>
        <div class="container">
    """
    
    for profile in profiles:
        html += f"""
            <div class="card">
                <div class="role-badge">{profile['profile_image']}</div>
                <h2>{profile['profile_name']}</h2>
                <p>{profile['profile_bio']}</p>
            </div>
        """
        
    html += """
        </div>
    </body>
    </html>
    """
    return html
