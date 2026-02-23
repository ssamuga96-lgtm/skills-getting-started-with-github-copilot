def test_signup_successfully_adds_participant(client, sample_email, sample_activity):
    # Arrange: A student and activity are ready

    # Act: Sign up the student
    response = client.post(
        f"/activities/{sample_activity}/signup?email={sample_email}"
    )

    # Assert: Signup succeeds and returns confirmation
    assert response.status_code == 200
    result = response.json()
    assert "Signed up" in result["message"]
    assert sample_email in result["message"]


def test_signup_adds_participant_to_activity(client, sample_activity):
    # Arrange: Get initial participant count and use a unique test email
    initial_response = client.get("/activities")
    initial_count = len(initial_response.json()[sample_activity]["participants"])
    unique_email = "counter-test@mergington.edu"

    # Act: Sign up the student
    client.post(f"/activities/{sample_activity}/signup?email={unique_email}")

    # Assert: Participant count increased
    final_response = client.get("/activities")
    final_count = len(final_response.json()[sample_activity]["participants"])
    assert final_count == initial_count + 1


def test_signup_fails_if_activity_not_found(client, sample_email, nonexistent_activity):
    # Arrange: An activity that doesn't exist

    # Act: Try to sign up for nonexistent activity
    response = client.post(
        f"/activities/{nonexistent_activity}/signup?email={sample_email}"
    )

    # Assert: Request fails with 404
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_signup_fails_if_already_signed_up(client, sample_activity):
    # Arrange: A student already in the activity (from seed data)
    existing_email = "michael@mergington.edu"  # Already in Chess Club

    # Act: Try to sign up again
    response = client.post(
        f"/activities/{sample_activity}/signup?email={existing_email}"
    )

    # Assert: Request fails with 400
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_with_special_characters_in_email(client, sample_activity):
    # Arrange: An email with special characters
    email = "test+tag@mergington.edu"

    # Act: Sign up with special character email
    response = client.post(
        f"/activities/{sample_activity}/signup?email={email}"
    )

    # Assert: Signup succeeds
    assert response.status_code == 200
