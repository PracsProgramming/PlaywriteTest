from .OrdersHistoryPage import OrdersHistoryPageClass


class DashboardPageClass:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderssHistoryPage = OrdersHistoryPageClass(self.page)
        return orderssHistoryPage
