from dashboard import DashboardPage


class LoginPage:

    def __init__(self,page):
        self.page = page
        # self.val =

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/")

    def login(self,user_Email,user_Password):

        self.page.get_by_placeholder("email@example.com").fill(user_Email)
        self.page.get_by_placeholder("enter your passsword").fill(user_Password)
        self.page.get_by_role("button", name="login").click()
        dashboardPage = DashboardPage(self.page)
        return dashboardPage
