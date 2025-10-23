if exist allure-results rmdir /s /q allure-results
pytest api/ tests/ -v --alluredir=allure-results
