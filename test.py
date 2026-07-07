from app import app

client = app.test_client()
response = client.post("/recommend", data={"movie": "Toy Story"})
data = response.get_json()

assert response.status_code == 200
assert data["status"] == "success"
assert len(data["recommendations"]) > 0
assert data["recommendations"][0]["title"].startswith("Toy Story")
print("Recommendation response includes the searched movie first")
