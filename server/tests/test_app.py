def test_index(client):
    rv = client.get('/')
    json_data = rv.get_json()
    assert json_data == {"message": "Hello, World!"}
