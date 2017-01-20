import subprocess as sp

import xmltodict

def queuedJobs(name_filter = ''):
        xml = sp.check_output(['qstat', '-u magic','-f', '-x']).decode()
        data = xmltodict.parse(xml)['Data']
        data = data['Job']

        data = [tmp for tmp in data if tmp['Job_Owner']=='magic@'+tmp['submit_host'] ]
        
        if filter != '':
            data = [tmp for tmp in data if tmp['Job_Name']==name_filter ]
        
        short = [tmp for tmp in data if tmp['queue'] == 'short']
        med = [tmp for tmp in data if tmp['queue'] == 'med']
        lo = [tmp for tmp in data if tmp['queue'] == 'long']

        short_running = [tmp for tmp in short if tmp['job_state'] == 'R']
        med_running = [tmp for tmp in med if tmp['job_state'] == 'R']
        lo_running = [tmp for tmp in lo if tmp['job_state'] == 'R']
        
        short_querry = [tmp for tmp in short if tmp['job_state'] == 'Q']
        med_querry = [tmp for tmp in med if tmp['job_state'] == 'Q']
        lo_querry = [tmp for tmp in lo if tmp['job_state'] == 'Q']
        
        return {'all':[len(short), len(med), len(lo)],
                'running':[len(short_running), len(med_running), len(lo_running)],
                'querry':[len(short_querry), len(med_querry), len(lo_querry)]}

