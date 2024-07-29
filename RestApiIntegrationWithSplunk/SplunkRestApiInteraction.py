import requests
import time

search_id = 'sid0001'
user_name = 'Suhas_j_c'
password = 'SjcSplunkCgs@999'


search_query = '''search index = main sourcetype="access_combined_wcookie"
                | stats count by status 
                | top 5 status showperc=false'''

post_data = {
    'id':search_id,
    'search':search_query,
    'output_mode' : 'json' # by default out is in xml format
}

splunk_search_url = r"https://172.31.144.1:8089/services/search/jobs"
res = requests.post(splunk_search_url, data=post_data, verify=False, auth=(user_name, password))

print(res.json())
# print(res.text) # return data in string


check_search_status_url = r"https://localhost:8089/services/search/jobs/{}".format(search_id)

is_search_completed = ''

while is_search_completed != 'DONE':
    time.sleep(5)
    search_status_res = requests.get(check_search_status_url, data={'output_mode' : 'json'},
                                     verify=False, auth=(user_name, password))

    search_status_res_data = search_status_res.json()

    is_search_completed = search_status_res_data.get('entry', [])[0].get('content', {}).get('dispatchState')

print("current search status is : {}".format(is_search_completed))


get_search_result_url = r"https://localhost:8089/services/search/jobs/{}/results/".format(search_id)

get_search_result_res = requests.get(get_search_result_url, data={'output_mode' : 'json'},
                                     verify=False, auth=(user_name, password))

result_data = get_search_result_res.json()

print(result_data)

for data in result_data.get('results'):
    print(data)

