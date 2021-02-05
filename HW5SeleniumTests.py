import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Chrome()

    '''
    Тест, который проверяет правильность статистики по ошибкам, а именно:
    Кол-во ошибок за текущий день не может превышать кол-во ошибок за целый месяц
    '''
    def test_status_page(self):
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(3)
        # Ищем кнопку Status
        elem = driver.find_element_by_link_text('Status')
        elem.click()
        # Статистика собирается долго( по крайней мере у меня), поэтому лучше подождать больше
        time.sleep(10)
        # Проверяем, что на статус странице есть статистика по системе
        self.assertIn('System Metrics', driver.page_source)
        # Получаем текстовые значения из метрик за день
        errorsText = driver.find_elements_by_css_selector('div.metric-average.color-secondary')
        # Получаем кол-во ошибок PyPI CDN Edge Errors за день
        pypiCDNEdgeErrorsPerDay = int(str(errorsText[0].get_attribute('innerHTML')).split(' ')[0].replace(',', ''))
        # Получаем кол-во ошибок PyPI Files CDN Edge Errors за день
        pypiFilesCDNEdgeErrorsPerDay = int(str(errorsText[1].get_attribute('innerHTML')).split(' ')[0].replace(',', ''))
        time.sleep(3)
        # Ищем элемент, который при нажатии на него покажет статистику за месяц
        elemsTimePeriod = driver.find_elements_by_css_selector(
            'a.timeframe.color-secondary.font-regular.border-color')
        monthTimePeriod = elemsTimePeriod[0]
        # Переходи на статистику за месяц
        monthTimePeriod.click()
        time.sleep(5)
        # Проверяем, что теперь активна статистика за месяц
        self.assertIn('active', monthTimePeriod.get_attribute('class'))
        # Получаем текстовые значения из метрик за месяц
        errorsText = driver.find_elements_by_css_selector('div.metric-average.color-secondary')
        # Получаем кол-во ошибок PyPI CDN Edge Errors за месяц
        pypiCDNEdgeErrorsPerMonth = int(str(errorsText[0].get_attribute('innerHTML')).split(' ')[0].replace(',', ''))
        # Получаем кол-во ошибок PyPI Files CDN Edge Errors за месяц
        pypiFilesCDNEdgeErrorsPerMonth = int(
            str(errorsText[1].get_attribute('innerHTML')).split(' ')[0].replace(',', ''))
        # Проверяем правильность статистики ( кол-во ошибок за месяц должно быть больше либо равно кол-ву за день)
        self.assertTrue(pypiFilesCDNEdgeErrorsPerMonth >= pypiFilesCDNEdgeErrorsPerDay
                        and pypiCDNEdgeErrorsPerMonth >= pypiCDNEdgeErrorsPerDay)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
