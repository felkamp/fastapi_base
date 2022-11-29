def test_1(client):
    response = client.get("/")

    assert response.status_code == 200


def test_2(client):
    response = client.get("/")

    assert response.status_code == 200
