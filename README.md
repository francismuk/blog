# BLOG
## An application that allows users to make your own blogs of any category and get feedback from other users as well as view random quotes. 8-7-2019


## By Francis Mukuha

## Description
This application is  a web application that allows users to submit a pitch. Also, other users are allowed to vote on submitted pitches and leave comments to give their feedback on the pitches. For a user to submit a pitch, vote on a pitch or give feedback on a pitch they need to have an account. <br>

The pitches are organized by categories. Examples of categories: <br>
- NEWS
- FICTION
- JOKES
- FASHION
- FOOD

## User Stories
As a user I would like:
* to view the different categories and add new ones
* to see the blogs other people have posted
* to submit a blog in any category
* to comment on the different blogs and leave feedback
* to view random quotes to give me inspiration as I blog

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email <br> Username <br> Password  | New user is registered and welcome email sent to the user |
| Log in | Your email <br> Password  | Logged in |
| Display blog categories | N/A | List of various blog categories |
| See blogs from selected category | **Click** add category | Directed to a page with a list of blogs from the selected category |
| Create a blog | **Click Create A Blog** | An authenticated user is directed to a page with a form where the user can create and submit a blog |
| See a blog | **Click** on a blog | A user is directed to a page containing the blog and its comments |
| Comment and give feedback on a blog | **Click Comment** | An authenticated user is directed to a page with a form where the user can create and submit a comment on a blogs |

## Prerequsites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
      (git clone https://github.com/francismuk/pitchers)
    - Edit the start.sh file with your api key from the news.org website
    - Install python 3.6
       (sudo apt-get install python3.6)
    - Run chmod a+x start.py
    - Run ./start.py


## Technologies used
    - Python 3.6
    - Quotes API
    - HTML
    - Bootstrap
    - CSS

### [MIT License](https://opensource.org/licenses/MIT)
Copyright (c) Francis Mukuha W
