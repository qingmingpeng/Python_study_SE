
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class DriverConfig:
    def driver_config(self):
        options = webdriver.ChromeOptions()
        # 设置窗口大小
        options.add_argument("window-size=1920,680")
        # 去除“Chrome正受到自动化测试的控制的提示”
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决se无法访问http的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")

        # 设置为无头模式:不打开浏览器也能进行自动化测试
        # options.add_argument("--headless")

        # 解决卡顿
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")



        #设置URL跟latest_release_URL的原因是 默认的URL是goggle的网址，是国外的网址 下载比较慢 换成国内的镜像  自动下载webdriver的镜像
        driver = webdriver.Chrome(ChromeDriverManager(url = "https://registry.npmmirror.com/-/binary/chromedriver",
                                                      latest_release_url = "https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                                      cache_valid_range=365).install(), options=options)
        #删除所有的cookies
        driver.delete_all_cookies()

        return driver




