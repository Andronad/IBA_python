import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramComSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    # Открывает страницу текущего аккаунта
    def openCurrentAcc(self):
        driver = self.driver

        accMenu = driver.find_element_by_css_selector('span._2dbep.qNELH')
        accMenu.click()
        time.sleep(1)

        accLink = driver.find_element_by_css_selector('a.-qQT3')
        accLink.click()
        time.sleep(3)

    # Ищет пользователя с заданным именем
    def searchFollower(self, name):
        driver = self.driver

        search = driver.find_element_by_css_selector('input.XTCLo.x3qfX')
        search.send_keys(name)
        time.sleep(2)

        accLink = driver.find_element_by_css_selector('a.-qQT3')
        accLink.click()
        time.sleep(3)

        self.assertIn(name, driver.page_source)

    '''
    Тест проверяет логирование и подписку\отписку от аккаунта в разных местах    
    '''

    def test_instagram_page(self):
        driver = self.driver
        driver.get("http://www.instagram.com")
        time.sleep(3)

        username = driver.find_element_by_name('username')
        username.send_keys('programma_zdorovia')

        password = driver.find_element_by_name('password')
        password.send_keys('Sergeevichprog')  # Неправильный пароль

        login = driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        login.click()
        time.sleep(5)

        self.assertIn('Sorry, your password was incorrect', driver.page_source)
        # Очищение поля password не работает через clear
        password.click()
        password.send_keys(Keys.LEFT_CONTROL, "a")
        time.sleep(1)
        password.send_keys('Sergeevichprog3')  # Правильный пароль

        login = driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        login.click()
        time.sleep(5)

        # Иногда всплывает окно, которое призывает активировать уведомления
        if 'Turn on Notifications' in driver.page_source:
            notNow = driver.find_element_by_css_selector('button.aOOlW.HoLwm')
            notNow.click()
            time.sleep(3)

        self.openCurrentAcc()

        countFollowing = driver.find_elements_by_css_selector('span.g47SY')[2].get_attribute('innerHTML')

        self.searchFollower('andronad13')

        followButton = driver.find_element_by_css_selector('button._5f5mN.jIbKX._6VtSN.yZn4P')
        followButton.click()
        time.sleep(3)

        self.assertIn('Message', driver.page_source)

        self.openCurrentAcc()

        countFollowingAfter = driver.find_elements_by_css_selector('span.g47SY')[2].get_attribute('innerHTML')

        self.assertEqual(int(countFollowing) + 1, int(countFollowingAfter))

        self.searchFollower('andronad13')

        unfollowButton = driver.find_element_by_css_selector('button._5f5mN.-fzfL._6VtSN.yZn4P')
        unfollowButton.click()
        time.sleep(1)

        confirmUnfollow = driver.find_element_by_css_selector('button.aOOlW.-Cab_')
        confirmUnfollow.click()

        self.assertIn('Follow', driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
