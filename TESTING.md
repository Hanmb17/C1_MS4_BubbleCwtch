# Bubble Cwtch - E-Commerce Site - Using Django

![Mock-up]()

#### **By Hannah Bowles**
[Click here to view the live web application](https://bubble-cwtch-7479c697eb91.herokuapp.com/)

The testing document for Bubble Cwtch

- - -
## Table of Contents

- [Introduction](#introduction)
- [Automated Testing](#automated-testing-using-test-driven-development)
- [Validation](#validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [JavaScript Linting](#javascript-linting)
    - [Python Linting](#python-linting)
    - [Accessibility Testing](#accessibility)
    - [Performance Testing](#performance)
- [Feature Testing](#feature-testing)
    - [Responsiveness/Device Testing](#responsiveness--devices)
    - [Browser Compatibility](#browser-compatibility)
    - [Feature Testing Results](#feature-testing-results)
- [User Stories Testing](#user-stories-testing)
- [Bugs and Fixes](#bugs--fixes)


---

## Introduction

I wanted implemented a thorough testing strategy combining both automated and manual testing methods. Below are the key aspects of the testing plan and the results obtained from testing on the [deployed site](https://bubble-cwtch-7479c697eb91.herokuapp.com/).

---

## Automated Testing

During development, I aimed to maintain a test-driven approach, which was my first experience with automated testing. Despite facing time constraints, I found automated testing to be a valuable tool in identifying issues and ensuring my code behaved as expected.

While the project is submitted, I plan to revisit it and write additional tests. Although I achieved a test coverage of 68%, I would have preferred to reach 100%. However, due to time limitations, I prioritised achieving a minimum viable product (MVP).

I enjoyed writing tests and using the coverage report to identify any missed lines, allowing me to create targeted tests for those areas. This approach proved effective in detecting bugs earlier in the development process, and I look forward to utilising it more in the future.

## Coverage Report

After running the coverage report, I generated the HTML coverage report, which enabled me to thoroughly explore and identify areas of my codebase that lacked sufficient test coverage, allowing me to prioritise and address these gaps when making more tests.

These are the commands I used to create the reports.
```bash
coverage run manage.py test
```

```bash
coverage html
```

My coverage result can me found here [Coverage Report](coverage_report.txt)

I used the follwing command to create this:

```bash
coverage report > coverage_report.txt
```

## Running Tests

I run tests for my Django project in the terminal. You can do this by navigating to the root directory of the project and use the following command:

### All Tests

```bash
python3 manage.py test
```

### All Tests In An App

Replace app_name with the name of the Django app

```bash
python3 manage.py test app_name
```

### A Specfic Test File

Replace app_name with the name of the Django app containing the test file, test_module with the Python module you want to run

```bash
pythona manage.py test app_name.test_module
```

- - -

## Validation

### HTML Validation

I used [W3 HTML Validator](https://validator.w3.org/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests.


### CSS Validation

I used [W3 CSS Validator](https://jigsaw.w3.org/css-validator/validator) to validate the style.css file and received no errors.

### JavaScript Linting

I used [JS Hint](https://jshint.com/) to validate my JavaScript code on all .js files within the project. I needed to add start my files with `/*jshint esversion: 6 */` to make sure jshint would treat the code by the standards of ES6. 


### Python Linting
I used the Code Institute [Python Linter](https://pep8ci.herokuapp.com/) to validate my python code in all files. A few warnings were noted with lines being too long or blank line issues, so these were amended. All files passed with no warnings after this.


### Accessibility

I used the [Wave Web Accessibility Evaluation Tool](https://wave.webaim.org/) to test the accessibility of the site. All pages passed with no errors, A few have warnings which I would look at improving in the future.


### Performance

I used the Lighthouse feature of Google Dev Tools to assess the scores of the site pages.