## Automated Amizone ATPC Checker
The students at my university were finding it hard to open our college portal twice a day and check for new placement opportunities listed on the Amity Training and Placement Cell (ATPC) Section on our Amizone Portal. So I designed this very simple script to check the Amizone portal every 1 hr and send a mail to everyone if any new opportunity is posted. 

### Tech Used and the Process
* **Selenium**: The Selenium Web Driver (chrome) is used to perform the following steps:
- Login to Amizone using credentials
- Wait for the Page to Load
- Find the ATPC Placement Button and Click It
- Find the Placements Button and Click It
- Read the Table on the Page
- Find the opportunity that has applications open.

* **Mailgun**: Through the Github Student Dev Pack, I got 20K mails per month limit, and so I decided to use it for the mailing mechanism. Once we identify the opportunity to share, we use the Mailgun API to queue the mails. Sadly there's no Python SDK yet for Mailgun.

* **AWS EC2**: The entire system is deployed on Amazon EC2 Free Tier Linux Instance.
  
* **PM2**: PM2 is used as the Process Manager, with a cron job setting for running the script every 1 hour. Startup settings have been configured so the script remains unaffected by EC2 restarts.
