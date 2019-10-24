"""配置包名和启动名"""
appPackage = "com.vcooline.aike"
appActivity = ".umanager.LoginActivity"


"""配置元素"""
from selenium.webdriver.common.by import By

login_username = By.ID, "com.vcooline.aike:id/etxt_username"
login_password = By.ID, "com.vcooline.aike:id/etxt_pwd"
login_btn = By.ID, "com.vcooline.aike:id/btn_login"


