# hybrid-automation-framework-selenium-pom
Example hybrid automation framework with Selenium and Python as coding language, with Pytest as test framework. <br>
The project implements Page Object Model (POM) and Data Driven Testing (DDT) along with HTTML Reports. <br>

## Functionallity
- open ebay
- choose category
- type query
- click search
- filtration of results
- scrap data of first n results

## How to run
1. cd (path to project directory)
```
pytest -v -s --browser (browser) --html=report.html

```
avaiable browsers:
- chrome
- firefox
- edge

For example

```
pytest -v -s --browser chrome --html=report.html

```

Note: -v -s --html=report.html are optional
