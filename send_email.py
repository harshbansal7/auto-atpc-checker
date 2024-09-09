import requests
from dotenv import load_dotenv
import os

load_dotenv()

def frame_email_and_send(data):
	company_name = data['company_name']
	registration_start = data['registration_start']
	registration_end = data['registration_end']
	data_file = data['data_file']
	counter = data['counter']
	
	# create a nice HTML message 
	html = f"""<!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            }}

            h2 {{
            color: #2C3E50;
            margin-bottom: 5px;
            }}

            p {{
            font-size: 14px;
            }}

            table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            }}

            table, th, td {{
            border: 1px solid #ddd;
            }}

            th, td {{
            padding: 12px;
            text-align: left;
            }}

            th {{
            background-color: #f2f2f2;
            color: #333;
            }}

            td a {{
            color: #2980B9;
            text-decoration: none;
            }}

            td a:hover {{
            text-decoration: underline;
            }}

            .footer {{
            margin-top: 10px;
            font-size: 13px;
            color: #555;
            }}

            .footer p {{
            margin: 5px 0;
            font-size: 10px;
            }}

            .signature {{
            font-size: 14px;
            margin-top: 20px;
            }}

            .signature p {{
                margin: 0;
                margin-bottom: 5px; /* or any desired value */
            }}
        </style>
        </head>
        <body>
        <h2>Placement Update: Batch 2025</h2>
        <p>A new opportunity has been added to your placement portal in the past hour. Please check the portal for more details.</p>
        
        <table>
            <tr>
            <th>Company Name</th>
            <th>Registration Start</th>
            <th>Registration End</th>
            <th>More Details</th>
            </tr>
            <tr>
            <td>{company_name}</td>
            <td>{registration_start}</td>
            <td>{registration_end}</td>
            <td><a href="{data_file}" target="_blank">Download</a></td>
            </tr>
        </table>

        <p>For more details, please visit the <a href="https://s.amizone.net" target="_blank">Amizone Portal</a>.</p>

        <div class="signature">
            <p>Regards,</p>
            <p><strong>Automated Amizone Checker</strong></p>
        </div>

        <div class="footer">
            <p>PS: So far, I have checked Amizone {counter} times for new updates! This automation is developed, deployed and maintained by Harsh Bansal.</p>
        </div>
        </body>
        </html>
    """
	return send_email(data, html)

def send_email(data, body_html):
    response = requests.post("https://api.mailgun.net/v3/mg.harshmakes.tech/messages", auth=("api", os.environ['MAILGUN_API_KEY']), data={"from": "ATPC Updates<noreply@mg.harshmakes.tech>", "to": ["harsh.bansal3@s.amity.edu", "shivangi.sharma8@s.amity.edu"],"subject": f"{data['company_name']} | Placement Update", "html": body_html})
    
    if response.status_code == 200:
        print(f"Email sent for {data['company_name']} with status code {response.status_code}")
        print(data)
        return True
    else:
        print(f"Error while sending email for {data['company_name']} with status code {response.status_code}")
        print(response.json())

        error_email = requests.post("https://api.mailgun.net/v3/mg.harshmakes.tech/messages", auth=("api", os.environ['MAILGUN_API_KEY']), data={"from": "ATPC Updates<noreply@mg.harshmakes.tech>", "to": ["harsh.bansal3@s.amity.edu", "harshbansal.contact@gmail.com"],"subject": "Error with ATPC Bot", "text": f"Error while sending email for {data['company_name']} with status code {response.status_code}"})
        
        if error_email.status_code == 200:
            return False
        else:
            print(f"Error while sending error email for {data['company_name']} with status code {error_email.status_code}")
            print(error_email.json())
            return False

    
