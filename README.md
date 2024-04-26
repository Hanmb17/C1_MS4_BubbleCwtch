# Bubble Cwtch - E-Commerce Site - Using Django

![Mock-up]()

#### **By Hannah Bowles**
[Click here to view the live web application](https://bubble-cwtch-7479c697eb91.herokuapp.com/)

Welcome to Bubble Cwtch, an e-commerce platform developed using Django, Python, JavaScript, CSS3 and HTML5. Created as part of Code Institute's Diploma in Web Application Development Course, Bubble Cwtch provides an online shopping experience featuring a handpicked range of artisanal bath bombs, soaps, and shower jellies.

- - -
## Table of Contents

- [Planning, Design & User Experience](#planning-design--user-experience)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
    - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frontend Frameworks / Libraries](#frontend-frameworks--libraries)
    - [Backend Modules / Packages & Frameworks](#backend-modules--packages--frameworks)
    - [Other Tools](#other-tools)
    - [External Sites / Resources / Software](#external-sites--resources--software)
- [Testing & Bugs](#testing--bugs)
- [Deployment](#deployment)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Deploying Your App](#deploying-your-app)
- [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Acknowledgments](#acknowledgments)


- - -

## Planning, Design & User Experience

I approached the planning and design of this project with a priority on providing a smooth user experience in line with e-commerce platform expectations. While ensuring I follow the principles of UX design and the five stages of strategy, scope, structure, skeleton and surface. My aim with Bubble Cwtch is to maintain the website's user-friendliness, visual appeal, and functionality in line with its original objectives while working to a deadline.

### Strategy

#### Project Aims

The primary aim of Bubble Cwtch is to provide customers with an intuitive platform to explore and purchase artisanal bath products. The website aims to showcase the unique range of bath bombs, soaps and shower jellies while providing efficient product and order management capabilities for the admin users.

#### Research

I conducted thorough research into similar websites within the cosmetics industry, as well as wider e-commerce sites. This research acted as a base for shaping the layout, design and functionality of Bubble Cwtch.

One significant influence was the product card design on Lush's website. After being inspired by Lush's product cards, I designed a similar product card for Bubble Cwtch that is attractive and user-friendly. Additionally, many websites included an 'add to bag' button in their product cards. Recognising the user benefits of this feature, I implemented it in Bubble Cwtch to simplify the shopping experience for users as it reduces the number of clicks required to purchase a product.

Websites visited for research:
- [Lush](https://www.lush.com/uk/en)
- [Bomb Cosmetics](https://bombcosmetics.co.uk/)
- [Pretty Suds](https://prettysuds.co.uk/)
- [Myddfai](https://myddfai.com/)
- [Adra](https://adrahome.com/)

####  User Stories

Below are the user stories I created after doing my research. These helped to guide the development and design.

1. As a general user:
  - 1.1: I want to understand the purpose of Bubble Cwtch immediately upon entering the website.
  - 1.2: I want to easily find products with intuitive navigation.
  - 1.3: I want Bubble Cwtch to be fully responsive for seamless browsing.
  - 1.4: I want to find Bubble Cwtch on social media for brand insights.
  - 1.5: I want effortless navigation back to the main site without relying on browser buttons if I encounter a non-existent page.
  - 1.6: I want to get feedback when interacting with Bubble Cwtch to confirm the success of my actions.

2. As a shopper:
  - 2.1: I want to browse Bubble Cwtch's products easily, with options to filter and search for specific items.
  - 2.2: I want to access more information about each product. 
  - 2.3: I want to be able to add a product to my bag quickly and with minimum clicks.
  - 2.4: I want to be able to shop for multiple items across Bubble Cwtch's product range.
  - 2.5: I want to be able to add multiples of a single product to my shopping bag at once.
  - 2.6: I want to be able to edit my shopping bag contents easily, adding or removing items as needed.
  - 2.7: I want to know the delivery charge for my order before proceeding to Checkout.
  - 2.8: I want my payment and order to be fully secure and trustworthy.
  - 2.9: I want the option to create an account on Bubble Cwtch to save my order history and track order status.

3. As a user with an account:
  - 3.1: I want my account on Bubble Cwtch to be secure and straightforward to set up.
  - 3.2: I want to see my order history easily, reviewing past purchases and tracking current orders.
  - 3.3: I want the ability to update and save my personal information within my account settings.
  - 3.4: I want to view the status of my order, allowing me to track its progress.

4. As an admin of the site:
  - 4.1: I want to be able to add and edit products easily.
  - 4.2: I want to the ability to remove products from sale, managing product availability.
  - 4.3: I want to be able to edit featured products.
  - 4.4: I want to be able to view all orders and filter by status.
  - 4.5: I want to be able to update the status of a customer's order easily. 
  - 4.6: I want to be easily navigate to the Django admin.
  - 4.7: I want the admin controls to blend with the site design but stand out.

- - -