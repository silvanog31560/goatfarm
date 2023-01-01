# goatfarm
This is a virtual goat gallery where the site owner can upload images and information about her goats. Starting with the index page, 
I used Django's Flatpages app to create it. For the Goat app I created three models, a Goat abstract base model, a Buck model, and a Doe model. 
I used a ForeignKey field to allow Nichole to create the parents and grandparents relationship. In this app I also used imagekit to create different
sized images and thumbnails. In the accounts app I created a custom user model and I also used SendGrid in the forms.py to allow for password reset
for the site admin. Next I created a Contact app to allow visitors to contact the admin. In this app I used SendGrid to email the message to the admin's
email. Finally I created a Review app to allow previous customers to leave a review, which is then displayed as a list.
