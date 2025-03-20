from playwright.sync_api import Playwright

order_payload = {
  "orders": [
    {
      "country": "India",
      "productOrderedId": "67a8dde5c0d3e6622a297cc8"
    }
  ]
}


class APIUtils:

    def get_token(self,playwright: Playwright):
        user_Email = "rahulshetty@gmail.com"
        user_Password = "Iamking@000"
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_Email, "userPassword": user_Password})
        assert response.ok
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self,playwright: Playwright):
        token = self.get_token(playwright)
        api_playwright_context =playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_playwright_context.post("/api/ecom/order/create-order",
                                    data=order_payload,
                                    headers={"Authorization":token,"content-Type":"application/json"})

        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id