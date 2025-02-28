from selenium.webdriver.common.by import By
from ai_ui.utils.report_generator import ReportGenerator

class UITestCase:
    def __init__(self, driver, ai_model):
        self.driver = driver
        self.ai_model = ai_model
        self.report_generator = ReportGenerator()

    def run_tests(self):
        self.test_login_page()
        self.generate_report()

    def test_login_page(self):
        try:
            # 打开登录页面
            self.driver.get("https://login.netease.com/connect/authorize?response_type=code&scope=openid%20nickname%20fullname%20email&client_id=59aba82296e111e8b9a35cf3fc97049c&state=3xmi7k648w&redirect_uri=https://dpp-kl.netease.com/api/kaola/v1/home/callback")
            self.driver.save_screenshot('screenshot.png')

            # 使用 AI 模型预测页面上元素的位置
            elements = self.ai_model.predict_elements('screenshot.png')
            print(f"预测的元素：{elements}")

            # 遍历所有预测的元素并执行相应的操作
            for element in elements:
                # AI 模型返回的元素细节，如（类型、位置、标签等）
                if element['type'] == 'button' and element['label'] == 'login':  # 假设 AI 可以预测到元素的类型和标签
                    login_button = self.driver.find_element(By.XPATH, element['xpath'])  # 使用动态 XPath 或其他定位方法
                    login_button.click()
                    print(f"点击了 {element['label']} 按钮。")
                    break  # 点击登录按钮后，停止继续处理其他元素

            # 使用 AI 预测点击登录按钮后的下一步操作
            context = "用户在登录页面，点击了登录按钮。"
            next_action = self.ai_model.predict_user_action(context)
            print(f"AI 预测的下一步操作：{next_action}")

            # 执行 AI 预测的操作
            if next_action == 'enter_username':
                username_field = self.driver.find_element(By.XPATH, self.ai_model.predict_element('screenshot.png', 'username'))
                username_field.send_keys("testuser")
            elif next_action == 'enter_password':
                password_field = self.driver.find_element(By.XPATH, self.ai_model.predict_element('screenshot.png', 'password'))
                password_field.send_keys("password123")
            elif next_action == 'submit':
                submit_button = self.driver.find_element(By.XPATH, self.ai_model.predict_element('screenshot.png', 'submit'))
                submit_button.click()

            self.report_generator.add_result("登录页面测试", "通过")
        except Exception as e:
            print(f"测试失败：{e}")
            self.report_generator.add_result("登录页面测试", "失败", str(e))

    def generate_report(self):
        self.report_generator.generate_html_report('reports/test_report.html')
