def test_get_activities_returns_all_activities(client):
    # Arrange: The activities endpoint is available

    # Act: Fetch all activities
    response = client.get("/activities")
    activities = response.json()

    # Assert: Response is successful and contains expected activities
    assert response.status_code == 200
    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert len(activities) == 9


def test_activity_has_required_fields(client):
    # Arrange: The activities endpoint is available

    # Act: Fetch activities and get the first one
    response = client.get("/activities")
    activities = response.json()
    chess_club = activities["Chess Club"]

    # Assert: Each activity has all required fields
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club


def test_activity_participants_is_list(client):
    # Arrange: We need to verify the participants structure

    # Act: Fetch activities
    response = client.get("/activities")
    activities = response.json()

    # Assert: Participants are in a list format
    for activity_name, activity in activities.items():
        assert isinstance(activity["participants"], list)
