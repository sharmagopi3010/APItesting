import requests, json, pytest


baseURL = "https://thetestingworldapi.com/"
def test_createUser():
    # adding student details
    student_detail_url = baseURL + "api/studentsDetails/"
    with open('studentdetails.json','r') as f:
        payload = json.loads(f.read())
    response = requests.post(student_detail_url,payload) #
    assert response.status_code == 201


    response_data = json.loads(response.text)
    user_id = response_data['id']
    print(user_id)
    
    # fetching student details
    getStudentinfo = student_detail_url+str(user_id)
    response1 = requests.get(getStudentinfo)

    assert response1.status_code == 200

    # adding technical infos for the same student
    tech_detail_url = baseURL+"api/technicalskills/"
    with open('technicaldetails.json','r') as f:
        tech_payload = json.loads(f.read())
        print(tech_payload)
        tech_payload['id'] = user_id
        print (tech_payload['id'])
        print(tech_payload)
        print(type(tech_payload['id']))
    response2  = requests.post(tech_detail_url,tech_payload)
    print(response2)

    get_tech_details =tech_detail_url+str(tech_payload['id'])
    response3 = requests.get(get_tech_details)
    print (response3.status_code)
    tech_get_details = json.loads(response3.text)
    print (tech_get_details)



    final_url = baseURL+"api/FinalStudentDetails/"+str(user_id)
    response3 = requests.get(final_url)
    assert response3.status_code == 200
    print(response3.text)