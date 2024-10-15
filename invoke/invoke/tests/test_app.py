from chalice.test import Client
from app import app

event = {
    "nome":"Barbara",
    "idade":"34"    
}

def test_index():
    with Client(app) as client:
        response = client.lambda_.invoke('Invoke', event)
        assert response.payload == True
