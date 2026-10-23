import app as app_module


def setup_client():
    app_module.app.config["TESTING"] = True
    return app_module.app.test_client()


def test_health_endpoint():
    response = setup_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "service": "CampusFix",
        "status": "healthy",
    }


def test_homepage_loads():
    response = setup_client().get("/")
    assert response.status_code == 200
    assert b"CampusFix" in response.data


def test_missing_page_returns_404():
    response = setup_client().get("/this-page-does-not-exist")
    assert response.status_code == 404
