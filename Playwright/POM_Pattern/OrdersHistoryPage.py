from .OrderDetailsPage import OrderDetailsPageClass


class OrdersHistoryPageClass:

    def __init__(self,page):
        self.page=page

    def selectOrder(self,OrderId):
        row = self.page.locator("tr").filter(has_text=OrderId)
        row.get_by_role("button", name="View").click()
        orderDetailsPage = OrderDetailsPageClass(self.page)
        return orderDetailsPage