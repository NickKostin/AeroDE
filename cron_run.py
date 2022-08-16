from crontab import CronTab
from pathlib import Path
from dotenv import dotenv_values

params = dotenv_values(Path(__file__).resolve().parent / '.env')
user = params['cron_user']
command = params['cron_command']

cron = CronTab(user=f'{user}')
job = cron.new(command=f'{command}')
job.hour.every(12)
cron.write()
