[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://snip-share.herokuapp.com/)&nbsp;
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)



<h1 align="center">Django-Cinema-Mall</h1>



## 	✈️ Introduction
* In this repo, I am creating complete Cinema mall backend API's with Django Rest Framework.

## 🚀 Technology Stack
* Backend
  * Python
  * Django 
  * Django Rest Framework
* Database
  * SQLite3

## 🛰️ Tech Stack Involved
<div style="display: flex;justify-content: center;">
<img height="64px" width="auto" src="https://image.flaticon.com/icons/svg/919/919852.svg">
 <br/>
<img height="64px" width="auto" src="https://twilio-cms-prod.s3.amazonaws.com/images/django-dark.width-808.png">
  <br/>
<div/>
 
 
# Installation Setup
First, clone the repository to your local machine:

```bash
git clone  git@github.com:samir321-pixel/Django_Cinema_Mall.git
```
# Install the requirements:
```bash
pip install -r requirements.txt
```

# run migrate

```bash
python manage.py migrate
```

# add gmail and password in settings.py
```
EMAIL_HOST_USER = 'yourgmailid.com'
EMAIL_HOST_PASSWORD = 'yourgmailpassword'
```

# create superuser

```bash
python manage.py createsuperuser
```

# Done!

Finally, run the development server:

```bash
python manage.py runserver

```
The project will be available at http://127.0.0.1:8000/



# 💹 Create Necessary data first for Start Booking Service Using Following API. 💹
* This API will be accessible by only Admin or Employee.
* Add, Update, Delete, Patch Movie : 
```/managecinema/cinema/```
* Add, Update, Delete, Patch slot For Movie : 
```/managecinema/cinema_arrange_slot/```
* Add, Update, Delete, Patch Movie Decks :
```/managecinema/cinema_deck/```
* Add, Update, Delete, Patch Movie Duration Slot : 
```/managecinema/cinema_slots_duration/```
* Add, Update, Delete, Patch Seat Name : 
```/cinema_booking/seat_manager/```

# ✏️ Customer Booking API's ✏️
* View List of seat present : 
```/cinema_booking/available_seat/```
* Book Seat : 
```/cinema_booking/book_seat/```

# 🏷️ Scope of project 🏷️
## Beta Version -
* Upcoming 3 days booking empty seat will be created as soon as admin or Employee create necessary slots.
* In each deck two empty seats are provided for each Time slots for upcoming 3 days.
* Only One Screen Provided.
* Customer able to book one seat at a time.
* Customer get notified as soon as he book slot in appilication notification panel as soon as through gmail notification.
* Yesterday or old slots get inactive according to current date and time so that user can only book upcoming slots seats.
* Customer can make rating and review for each cinema.

## Full Version -
* Get Any number of Screen according to Need.
* Get Any Number of decks, seats.
* Integration of Paytm.
* Book multiple seats at single time.
* Cancel Booking feature.

## 🌏 Browser Support

| <img src="https://user-images.githubusercontent.com/1215767/34348387-a2e64588-ea4d-11e7-8267-a43365103afe.png" alt="Chrome" width="16px" height="16px" /> Chrome | <img src="https://user-images.githubusercontent.com/1215767/34348590-250b3ca2-ea4f-11e7-9efb-da953359321f.png" alt="IE" width="16px" height="16px" /> Internet Explorer | <img src="https://user-images.githubusercontent.com/1215767/34348380-93e77ae8-ea4d-11e7-8696-9a989ddbbbf5.png" alt="Edge" width="16px" height="16px" /> Edge | <img src="https://user-images.githubusercontent.com/1215767/34348394-a981f892-ea4d-11e7-9156-d128d58386b9.png" alt="Safari" width="16px" height="16px" /> Safari | <img src="https://user-images.githubusercontent.com/1215767/34348383-9e7ed492-ea4d-11e7-910c-03b39d52f496.png" alt="Firefox" width="16px" height="16px" /> Firefox |
| :---------: | :---------: | :---------: | :---------: | :---------: |
| Yes | 10+ | Yes | Yes | Yes |



## 🏆 Project Admin 🏆
[![Maintenance](https://img.shields.io/maintenance/yes/2020?color=green&logo=github)](https://github.com/samir321-pixel)

> **_Need help?_ 🤔** 
> **_Feel free to contact me @ [saitwalsamir@gmail.com](mailto:saitwalsamir@gmail.com?Subject=Library_Project)_**

## Like This?? Star ⭐ this Repo.

## 👮 **_For Full Version contact me @ [saitwalsamir@gmail.com](mailto:saitwalsamir@gmail.com?Subject=Library_Project)_** 👮

> Made By Samir Saitwal with ❤️

> Samir Saitwal &copy; 2021
<br><br>
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/samir321-pixel)
[![ForTheBadge built-by-developers](http://ForTheBadge.com/images/badges/built-by-developers.svg)](https://github.com/samir321-pixel)









***
## 📘 Useful Resources 📘
- [Django Docs](https://docs.djangoproject.com/en/3.0/)
- [Django Rest Framework Docs](https://www.django-rest-framework.org/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide)
## 💻 Tools 💻

<a href="gui-tool-tutorials/github-desktop-tutorial.md"><img alt="GitHub Desktop" src="https://desktop.github.com/images/desktop-icon.svg" width="100"></a> 
<a href="gui-tool-tutorials/github-windows-vs-code-tutorial.md"><img alt="VS Code" src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Visual_Studio_Code_1.18_icon.svg" width=100></a> &nbsp;
<a href="#"><img alt="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/PyCharm_Logo.svg/512px-PyCharm_Logo.svg.png" width=100></a> &nbsp;
<a href="#"><img alt="Pycharm" src="https://miro.medium.com/max/512/1*fVBL9mtLJmHIH6YpU7WvHQ.png" width=100></a>


