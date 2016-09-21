import requests,json


def task(msg):
    """ 
    - Talks to tropo API
    """
    
    data = '{"name":"https://scripts.cisco.com/ui/use/my_conversation_2","question":msg}'

    res = requests.post(url='https://scripts.cisco.com/api/v1/jobs',
                        data=data,
		            auth=('rram','whatever password'),
                    headers={'Content-Type': 'application/json'})
    
    
    url = "https://api.tropo.com/1.0/sessions?action=create&token=56477965796c6b53416b71416354484b6a584b466d426d6f4a6f524f6a43516b6c454f695349456d484f6f61"
    output = requests.post(url, headers={'content-type': 'application/x-www-urlencoded'},data=res.json())
    print(output)
   
