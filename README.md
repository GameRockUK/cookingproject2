# Cooking Project

The project is designed to allow users the ability to create, edit and delete recipies, the project would be for the cooking world and maintained by
the cooking world.

With easy-to-use functionality and mobile friendly approach, no matter what device you are on you can lookup recipes, add them and edit them
if you think the recipe could be improved.

## UX

The website is for all users who wish to create new, edit and delete recipes. 

As a Chef, I want the ability to create, edit and delete recipes so I can access them wherever I am and be able to refer back to them. My
goal is for the create, edit and delete functionality of recipes to work. The business goal is to create a community where users can create recipes
and build database of recipes.

Wireframe/Mockup for this is: https://ibb.co/mJ8tTxn

## Features

### Existing Features:

Create Recipe - Using a Modal and some Materialise CSS we have created a Modal form so that the users don't get redirected around the place,
we feel like this is a good feature.

Edit Recipe - Edit recipe function allows the users to edit any recipe on-site and make changes to them at any time. 

Delete Recipe - This function allows the customers to delete any recipes which may not be required anymore.

### Features left to Implement:

- Allow only the Recipe owner to be able to edit/delete the Recipe.
- Allow image of the recipes to be uploaded so that users can see the end product.


## Technologies Used

The Technologies used in this project are:

- Materialise CSS
- JQuery
- MongoDB
- Heroku
- Python/HTML/CSS/Javascript Programming Languages

Main issue with the application is that it allows anyone to do anything, if time provided we would restrict it down to just the recipe owner could
edit/delete the recipe they have created.

## Testing

We have done various tests to ensure this application reaches the expectation of the customers. 

The first test we did was the basic functionality of the add, edit and delete recipes functions. We identified early on that the data from the MongoDB wasn't being manipulated
as we would of liked and the communication between the application and the MongoDB was working, after tweaking the app.py we realised that the env.py was incorrect so we adjusted this
to make it work, it turned out it was the Mongo URI which was incorrect.

Another test we did was the responsive test, to ensure the application worked across other resolutions. We hit a few issues with this, particularly around the Paralax that we added. We had to
adjust the width in the stylesheet and we also had to edit the background image width as well. After a few styling tweaks we managed to get it working as expected.

## Deployment

We deployed the application to Github and Heroku, Github for the version control and backup purposes and Heroku for the publishing of the application. 

In Heroku we had to add the Mongo URI into the config vars to ensure it connected with the MongoDB correctly.

In order to run the code locally we used the git command 'python3 app.py' on Gitpod.

## Credits

Materialise CSS for code taken for the Modal, Navbar styling and form design. MongoDB for providing database and Heroku for providing an
application deployment service for our application to run on.