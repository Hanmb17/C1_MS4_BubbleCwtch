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

### Scope

Using the user stories, I created a list of features I would like to add to the site to meet my user stories.

| Feature                                                  | Difficulty | Importance |
|----------------------------------------------------------|------------|------------|
| **Navigation:**                                          |            |            |
| Responsive Design                                       | 1          | 5          |
| Navigation - all page links                             | 1          | 5          |
| Navigation - search facility                            | 3          | 4          |
| **Footer:**                                              |            |            |
| Footer - company info                                   | 1          | 3          |
| Footer - social links                                   | 1          | 3          |
| **Home Page:**                                           |            |            |
| Home Page - branding & explanatory text                 | 1          | 4          |
| Home Page - Featured Products                           | 2          | 2          |
| **Product Management:**                                 |            |            |
| Products - Product cards with summary info              | 2          | 5          |
| Products - Product cards with add to bag button         | 2          | 4          |
| Products - Sorting/searching/filtering                  | 5          | 4          |
| Products - Detail Page with more info                   | 2          | 5          |
| Products - Detail Page add to bag & quantity select     | 4          | 5          |
| Products - CRUD functionality for admins                | 3          | 5          |
| **Shopping Bag and Checkout:**                          |            |            |
| Bag - Users can store items in a bag for purchase       | 4          | 5          |
| Bag - Users can edit product quantity and remove        | 3          | 5          |
| Checkout - Page with bag summary and delivery info      | 4          | 5          |
| Checkout - Secure payment system                        | 5          | 5          |
| Checkout - Page to show order summary on successful checkout | 3        | 3          |
| **User Accounts:**                                      |            |            |
| User accounts - all standard login/out/register functionality | 4     | 5          |
| User accounts - secure & reliable                      | 4          | 5          |
| Profile - User profile page showing order history      | 3          | 4          |
| Profile - Page to show historical order information    | 2          | 3          |
| Profile - Users can save & update their info for future orders | 4     | 4          |
| **Admin Section:**                                      |            |            |
| Links in main navigation                               | 2          | 4          |
| Profile - Filter/view all orders                       | 3          | 4          |
| Profile - Click through to view and edit order status          | 4          | 4          |
| Admin sections have a different look                   | 3          | 3          |

---

### Structure

- - -

### Skeleton
Add Diagram

#### Database Schema

Add Diagram

#### Models


<details><summary>UserProfile Model</summary>

| **Field**                | **Field Type** | **Validation**                          | **null** | **blank** | **default** | **on_delete** | **editable** | **related_name** |
|--------------------------|----------------|-----------------------------------------|----------|-----------|-------------|---------------|--------------|------------------|
| **User**                 | OneToOneField  | 'User', on_delete=models.CASCADE       | FALSE    | FALSE     | n/a         | CASCADE       | TRUE         | n/a              |
| **Default Phone Number** | Char           | max_length=20                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default Country**      | Char           | max_length=2                            | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default Postcode**     | Char           | max_length=20                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default Town or City** | Char           | max_length=40                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default Street Address1** | Char       | max_length=80                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default Street Address2** | Char       | max_length=80                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Default County**       | Char           | max_length=80                           | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |

</details>

<details><summary>Category Model</summary>

| **Field**         | **Field Type** | **Validation** | **null** | **blank** | **default** | **on_delete** | **editable** | **related_name** |
|-------------------|----------------|----------------|----------|-----------|-------------|---------------|--------------|------------------|
| **Name**          | Char           | max_length=254 | FALSE    | n/a       | n/a         | n/a           | TRUE         | n/a              |
| **Friendly Name** | Char           | max_length=254 | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |

</details>

<details><summary>Product Model</summary>

| **Field**         | **Field Type** | **Validation**                           | **null** | **blank** | **default** | **on_delete** | **editable** | **related_name** |
|-------------------|----------------|------------------------------------------|----------|-----------|-------------|---------------|--------------|------------------|
| **Category**      | ForeignKey     | 'Category', null=True, on_delete=SET_NULL| TRUE     | TRUE      | n/a         | SET_NULL      | TRUE         | n/a              |
| **Name**          | Char           | max_length=254                           | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Description**   | Text           |                                          | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Price**         | Decimal        | max_digits=6, decimal_places=2           | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Rating**        | Integer        | validators=[MaxValueValidator(5), MinValueValidator(0)] | TRUE | TRUE      | 0           |               | TRUE         | n/a              |
| **Is Featured**   | Boolean        | default=False                            | FALSE    | TRUE      | FALSE       |               | TRUE         | n/a              |
| **Discontinued**  | Boolean        | default=False                            | FALSE    | TRUE      | FALSE       |               | TRUE         | n/a              |
| **Image URL**     | URLField       | max_length=1024, null=True               | TRUE     | TRUE      | n/a         |               | TRUE         | n/a              |
| **Image**         | ImageField     | null=True, blank=True                    | TRUE     | TRUE      | n/a         |               | TRUE         | n/a              |


</details>

<details><summary>Order Model</summary>

| **Field**          | **Field Type** | **Validation**                             | **null** | **blank** | **default** | **on_delete** | **editable** | **related_name** |
|--------------------|----------------|--------------------------------------------|----------|-----------|-------------|---------------|--------------|------------------|
| **Order Number**   | Char           | max_length=32                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Full Name**      | Char           | max_length=50                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Email**          | Char           | max_length=254                             | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Phone Number**   | Char           | max_length=20                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Street Address1**| Char           | max_length=80                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Street Address2**| Char           | max_length=80, null=True, blank=True       | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Town or City**   | Char           | max_length=40                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **County**         | Char           | max_length=80, null=True, blank=True       | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Postcode**       | Char           | max_length=20, null=True, blank=True       | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Country**        | Char           | max_length=2                               | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Date**           | DateTime       |                                            | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Order Total**    | Decimal        | max_digits=10, decimal_places=2            | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Delivery Cost**  | Decimal        | max_digits=10, decimal_places=2            | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Grand Total**    | Decimal        | max_digits=10, decimal_places=2            | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Original Bag**   | Text           |                                            | TRUE     | TRUE      | n/a         | n/a           | TRUE         | n/a              |
| **Stripe PID**     | Char           | max_length=254                             | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **User Profile**   | ForeignKey     | 'UserProfile', null=True, on_delete=SET_NULL| TRUE    | TRUE      | n/a         | SET_NULL      | TRUE         | n/a              |
| **Status**         | Char           | max_length=20                              | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |


</details>

<details><summary>Orderline Model</summary>

| **Field**          | **Field Type** | **Validation**                          | **null** | **blank** | **default** | **on_delete** | **editable** | **related_name** |
|--------------------|----------------|-----------------------------------------|----------|-----------|-------------|---------------|--------------|------------------|
| **Order**          | ForeignKey     | 'Order', on_delete=models.CASCADE      | FALSE    | FALSE     | n/a         | CASCADE       | TRUE         | n/a              |
| **Product**        | ForeignKey     | 'Product', on_delete=models.PROTECT     | FALSE    | FALSE     | n/a         | PROTECT       | TRUE         | n/a              |
| **Quantity**       | Integer        |                                         | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |
| **Line Item Total**| Decimal        | max_digits=10, decimal_places=2         | FALSE    | FALSE     | n/a         | n/a           | TRUE         | n/a              |

</details>

---

### Surface

#### Wireframes

Add wireframes 

#### Colour

Add colour info

### Typography

The website uses two typefaces that I felt worked well together and matched the playfulness of the brand while complementing each other::

- **Headings & Site Logo**: [Fredoka](https://fonts.google.com/specimen/Fredoka) - Fredoka's playful and bold characteristics make it great for the headlines and site logo.

- **Main Body Text**: [Poppins](https://fonts.google.com/specimen/Poppins) - Poppins offers excellent readability, making it perfect for the main body content.

These typefaces work together to create a cohesive and visually pleasing user experience,  helping to improve the overall design.

- - -

#### Images & Graphics

##### Logo


#### Design Changes

##### Admin Forms Background colour

##### Edit / Delete Product Buttons on Cards


### Features

Here's a breakdown of the features on the Bubble Cwtch Site

#### Meta Tags
- **Functionality**: All pages have title and description meta tags, enhancing SEO performance.
- **Value To User**: This ensures easy discovery by online shoppers and provides clarity on the site's purpose and content.

#### Layout
- **Functionality**: Site utilises Bootstrap container to restrict site width for optimal display.
- **Value To User**: Ensures consistent and visually appealing display across devices, enhancing user experience and eliciting a positive emotional response.

#### General Responsiveness
- **Functionality**: Full responsiveness across all pages, including font size adjustments, padding & margin tweaks, and layout modifications for varying screen sizes.
- **Value To User**: Ensures seamless navigation and visual appeal on any device, contributing to a positive user experience.

#### Favicon
- **Functionality**: Incorporates a favicon featuring the brand's logo.
- **Value To User**: Builds brand consistency, enhances professionalism and instils trustworthiness in the site.

#### Nav Bar
- **Functionality**: Responsive navigation bar with custom layouts and content for different screen sizes.
- **Value To User**: Facilitates easy navigation regardless of device, offers search functionality and provides feedback on shopping bag contents.

#### Delivery Banner
- **Functionality**: Persistent banner across all pages indicating the free delivery threshold.
- **Value to User**: Encourages higher spending, informs users about free delivery and boosts sales.

#### Buttons and Links
- **Functionality**: Consistently styled buttons and links with specific colours for different actions.
- **Value To User**: Provides intuitive UI and reduces mistakes during interactions.

#### Messages
- **Functionality**: Utilises the Django messaging framework and Bootstrap's Toast element for user feedback throughout the site.
- **Value To User**: Offers reassurance, enhances user experience and promotes a sense of security.


Add page info here and revert back to user stories 


#### Feature Information

Talk about reviews - adding ingredients - recipes for admin and inventory 
Back to top button


- - -

## Technologies Used

### Languages

- [HTML:](https://en.wikipedia.org/wiki/HTML5) Used for the site's structure and content.
- [CSS:](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) Used to style the website (along side Bootstrap)
- [JavaScript:](https://en.wikipedia.org/wiki/JavaScript) Used for interactive features such as:
  - Bag / Product Quantity Input
  - Stripe Payment Handling
  - Product form image field text
  - Product sorting page reload
  - Remove & Update products from bag
- [Python: ](<https://en.wikipedia.org/wiki/Python_(programming_language)>) Used to build the core of the backend of the project within the Django framework


### Web Development Frameworks

- [Django:](https://www.djangoproject.com/) High Level Python-based Web Framework.
- [Bootstrap:](https://getbootstrap.com/) Ensures consistent styling, layout, and responsiveness throughout the site.
- [Font Awesome:](https://fontawesome.com/) Adds icons for improved user experience and visual appeal.
- [JQuery:](https://jquery.com/) Simplifies JavaScript coding for quicker development.


### Database and Database Hosting

- [SQLITE:](https://docs.djangoproject.com/en/4.1/ref/databases/#sqlite-notes) Built-in Django database for development.
- [Elephant SQL:](https://www.elephantsql.com/) PPostgres-based database host for live production app.


### Additional Backend Tools

- [AllAuth:](https://django-allauth.readthedocs.io/en/latest/) Integrated Django authentication and sign-in.
- [Django Countries:](https://pypi.org/project/django-countries/) Provides country choices for forms.
- [Django Widget Tweaks:](https://pypi.org/project/django-widget-tweaks/) Customizses form field styling.
- [Django Storages:](https://django-storages.readthedocs.io/en/latest/) Offers custom storage backends for Django.
- [Freezegun:](https://pypi.org/project/freezegun/) Aids automated testing with datetime control.
- [Gunicorn:](https://gunicorn.org/) Python WSGI HTTP Server for UNIX.
- [Pillow:](https://pypi.org/project/Pillow/) Extends image handling capabilities.
- [Psycopg2:](https://www.psycopg.org/) Facilitates smooth communication between backend and database.
- [s3transfer:](https://pypi.org/project/s3transfer/) Manages Amazon AWS S3 Transfers.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) & [Botocore:](https://github.com/boto/botocore) Configures AWS services using Python.
- [Stripe:](https://stripe.com/gb) Manages secure online payments.
- [dj-database-url:](https://pypi.org/project/dj-database-url/) Enables DATABASE_URL env variable usage in settings.py.
- [Coverage:](https://coverage.readthedocs.io/en/7.3.1/) Measures code coverage of Python programs.
- [oauthlib](https://pypi.org/project/oauthlib/) & [requests-oauthlib:](https://pypi.org/project/requests-oauthlib/) Handles authentication via OAuth.
- [python3-openid:](https://pypi.org/project/python3-openid/) Supports the use of the OpenID decentralized identity system.
- [sqlparse:](https://pypi.org/project/sqlparse/) Parses SQL for Python.
- [urllib3:](https://pypi.org/project/urllib3/) HTTP client for Python.


### Development, Deployment and testing 

- [Git:](https://git-scm.com/) Version control for collaborative development.
- [GitHub:](https://github.com/) Hosts the project code.
- [Gitpod:](https://www.gitpod.io/) Provides a development environment for coding and testing.
- [Heroku:](https://dashboard.heroku.com/apps) Deploys the live site.
- [Amazon Web Services:](https://aws.amazon.com/) Hosts static files and images for the live production site.
- [Google Chrome Dev Tools:](https://www.google.com/intl/en_uk/chrome/) Inspects page elements, debugs issues, and tests responsiveness.
- [Temp Mail:](https://temp-mail.org/en/) Generates temporary emails for testing account verification and order confirmation.


### Creative Resources

- [Google Fonts:](https://fonts.google.com/) Used to select & import the fonts
- [Lucidchart](https://www.lucidchart.com/pages/) To create the flow diagram of the website
- [DrawSQL](https://drawsql.app/) Used to visually design the database schema
- [ChatGPT:](https://chat.openai.com/auth/login) Used to generate copy to populate site (not used for any code)
- [Affinity Photo:]() Used to create 
- [Affinity Designer:]() Used to create the site logo
- [Tiny PNG:](https://tinypng.com/) Optimises images for reduced file size
- [ezGIF:](https://ezgif.com/) Creates GIFs for the README.
- [Favicon.io:](https://favicon.io/favicon-converter/) Generates and adds the favicon.

