from selenium import webdriver
from tests.test_cases import UITestCase
from ai_model.model import AIModel

def main():
    # 初始化WebDriver
    driver = webdriver.Chrome()  # 确保已安装ChromeDriver或相应驱动

    # 初始化AI模型
    ai_model = AIModel()

    # 初始化测试用例
    ui_test_case = UITestCase(driver, ai_model)

    # 运行测试
    ui_test_case.run_tests()

    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    main()