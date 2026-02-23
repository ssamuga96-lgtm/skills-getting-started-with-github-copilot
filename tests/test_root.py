def test_root_redirects_to_static_index(client):
    # Arrange: The root endpoint is ready

    # Act: Request the root path
    response = client.get("/", follow_redirects=False)

    # Assert: Should redirect to /static/index.html
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"
