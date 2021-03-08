from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://cdn1.python3.vip/files/selenium/sample3.html")
driver.find_element_by_xpath('//a').click()
# print(driver.title)
# 保存当前窗口的句柄
mainWindow = driver.current_window_handle
# print(driver.window_handles)  # ['CDwindow-CC99DA62D98C6661D3BBE851F0DF589B', 'CDwindow-331ACA717F14151702A2E35401736BE1']
for handle in driver.window_handles:
    # 先切换到该窗口
    driver.switch_to.window(handle)
    # 取该窗口的标题栏字符串，判断是不是要操作的那个窗口
    if "bing" in driver.title:
        # # 如果是，那么这时候WebDriver对象就是对应的该窗口，正好，跳出循环，
        break
# 通过前面保存的老窗口的句柄，自己切换到老窗口
time.sleep(10)
driver.switch_to.window(mainWindow)
time.sleep(3)
driver.quit()
