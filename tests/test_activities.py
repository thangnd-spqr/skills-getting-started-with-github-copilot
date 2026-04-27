def test_get_activities_returns_dict(client):
    # Arrange: client fixture provided
    # Act
    resp = client.get("/activities")
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_post_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Club"
    email = "student@example.com"
    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert resp.status_code == 404
    assert resp.json().get("detail") == "Activity not found"
