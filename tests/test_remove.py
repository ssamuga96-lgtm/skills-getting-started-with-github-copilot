def test_remove_participant_successfully(client, sample_email, sample_activity):
    # Arrange: First sign up a participant
    client.post(f"/activities/{sample_activity}/signup?email={sample_email}")

    # Act: Remove the participant
    response = client.delete(
        f"/activities/{sample_activity}/signup?email={sample_email}"
    )

    # Assert: Removal succeeds
    assert response.status_code == 200
    assert "Removed" in response.json()["message"]


def test_remove_decreases_participant_count(client, sample_email, sample_activity):
    # Arrange: Sign up a participant and get initial count
    client.post(f"/activities/{sample_activity}/signup?email={sample_email}")
    pre_remove = client.get("/activities").json()[sample_activity]["participants"]

    # Act: Remove the participant
    client.delete(f"/activities/{sample_activity}/signup?email={sample_email}")

    # Assert: Participant count decreased
    post_remove = client.get("/activities").json()[sample_activity]["participants"]
    assert len(post_remove) == len(pre_remove) - 1
    assert sample_email not in post_remove


def test_remove_fails_if_activity_not_found(client, sample_email, nonexistent_activity):
    # Arrange: An activity that doesn't exist

    # Act: Try to remove from nonexistent activity
    response = client.delete(
        f"/activities/{nonexistent_activity}/signup?email={sample_email}"
    )

    # Assert: Request fails with 404
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_remove_fails_if_not_signed_up(client, sample_activity):
    # Arrange: A student not signed up for the activity
    email = "notregistered@mergington.edu"

    # Act: Try to remove them
    response = client.delete(
        f"/activities/{sample_activity}/signup?email={email}"
    )

    # Assert: Request fails with 400
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]
