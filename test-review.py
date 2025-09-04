import pytest
import requests
from playwright.sync_api import expect
import allure

BASE_URL = "https://jsonplaceholder.typicode.com"

@allure.suite("API and UI Integration Tests")
class TestIntegration:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page
    
    @allure.title("Create post via API and verify in UI")
    def test_create_post_and_verify(self):
        # API Part
        with allure.step("Create new post via API"):
            payload = {
                "title": "Test Post",
                "body": "This is a test post",
                "userId": 1
            }
            response = requests.post(f"{BASE_URL}/posts", json=payload)
            assert response.status_code == 201
            post_id = response.json()["id"]
        
        # UI Part
        with allure.step("Verify post in UI"):
            self.page.goto(f"{BASE_URL}/posts/{post_id}")
            
            title = self.page.locator("h1").inner_text()
            assert title == payload["title"]
            assert self.page.get_by_text(payload["body"]).is_visible()

    @allure.title("Get user data and verify UI elements")
    @pytest.mark.parametrize("user_id", [1, 2, 3], ids=lambda x: f"user{x}")
    def test_user_data_verification(self, user_id):
        # API Request
        with allure.step(f"Get user data for ID {user_id}"):
            response = requests.get(f"{BASE_URL}/users/{user_id}")
            assert response.status_code == 200
            user_data = response.json()
        
        # UI Verification
        self.page.goto("https://demoqa.com/profile")
        self.page.fill("#userInput", user_data["username"])
        self.page.click("#submitButton")
        
        email = self.page.locator("#emailValue").inner_text(timeout=100)
        assert email == user_data["email"]

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "viewport": {"width": 1920, "height": 1080}}
