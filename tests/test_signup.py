def test_successful_signup_follows_aaa(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@mergington.edu"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert "Signed up" in resp.json().get("message", "")


def test_duplicate_signup_returns_400(client):
    # Arrange
    activity = "Programming Class"
    email = "duplicate@mergington.edu"

    # Act - first signup
    resp1 = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Act - duplicate signup
    resp2 = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp1.status_code == 200
    assert resp2.status_code == 400
    assert resp2.json().get("detail") == "Student already signed up"


def test_unregister_removes_participant(client):
    # Arrange
    activity = "Gym Class"
    # pick an existing participant from the seeded data
    existing = "john@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": existing})

    # Assert
    assert resp.status_code == 200
    assert "Unregistered" in resp.json().get("message", "")
    # verify removed
    get_resp = client.get("/activities")
    participants = get_resp.json()[activity]["participants"]
    assert existing not in participants
