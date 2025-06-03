import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope='module')
def api_client():
    return APIClient()

def test_getuser_validation(api_client):
    response = api_client.get('users')
    print(response.json())
    assert response.status_code==200
    assert len(response.json())>0

def test_create_user(api_client,load_test_data):
    #user_data={
       # "name":"supriya",
      #  "username":"qa_user",
     #   "email":"test@email.com"
    #}
    user_data=load_test_data["new_user"]
    unique_email=f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"]=unique_email
    response = api_client.post('users',user_data)
    print(response.json())
    assert response.status_code==201
    assert response.json()['name']=='supriya B'
    id=response.json()['id']
    responseget=api_client.get('users/10')
    print(response.json())
    assert responseget.status_code==200
   # assert len(response.json())>0
#
def test_update_user(api_client):
    user_data={
        "name":"supriya B",
        "username":"qa_user",
        "email":"test@emil.com"
    }
    response = api_client.put('users/1',user_data)
    print(response.json())
    assert response.status_code==200
    assert response.json()['name']=='supriya B'

def test_delete_user(api_client):
    response = api_client.delete('users/1')
    print(response.json())
    assert response.status_code==200
