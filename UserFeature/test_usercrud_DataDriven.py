import requests, json, pytest
from UserFeature import Library



baseURL = "https://thetestingworldapi.com/"
def test_createUser():
    # adding student details
    student_detail_url = baseURL + "api/studentsDetails/"
    with open('studentdetails.json','r') as f:
        payload = json.loads(f.read())

    obj = Library.Common('student_data.xlsx','Sheet1')
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keyList = obj.fetch_key_names()

    for i in range (2, row+1):
        updated_json_request = obj.update_request_with_data(i,payload,keyList)
        response = requests.post(student_detail_url,updated_json_request)
        print(response.status_code)