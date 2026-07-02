from fastapi.testclient import TestClient

from src import app as app_module


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"
    app_module.activities[activity_name]["participants"] = [
        participant_email,
        "daniel@mergington.edu",
    ]

    client = TestClient(app_module.app)
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": participant_email},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Removed {participant_email} from {activity_name}"
    }
    assert participant_email not in app_module.activities[activity_name]["participants"]
