# The Cookbook App  

The idea behind this project was to create an online cookbook app using python and either SQL or MongoDB.  
The main functionality of the app is to allow users to look up exsisting recipes, have the  
ability too add and edit existing recipes, and to delete any that were no longer requires.  
[View the project here](https://craigs-cookbook.herokuapp.com/).

### UX

* User Stories
    * First Time Visitor Goals
        1. As a first time user I should be able to signup and login easily.
        1. A first time user should be able to navigate the app without confusion.
        1. As a first time visitor to the app I should be able to see my saved recipes instantly
        so i can reference them as I cook

    * Returning Visitor Goals
        1. Returning users must be able to edit and update saved recipes to make adjustments to the recipes
        1. As a returning user I should be able to delete recipes I didn't like
        1. As a returning visitor I am able to add new recipes through a form quickly

* design   
    * Colour scheme
        I went for a green on white colour scheme as this expresses the feeling of freshness and cleanlness
        when it comes to food.
    
    * Typography 
        I choose Roboto and Roboto slab for my text because they are some of the most popular fonts at this time.

    * Imagery 
        Images are important in this app because users need to see what the meals look like before they make them.
        It is often said you eat with your eyes.

* Wireframe And Database Schema
    1. [wireframe](https://github.com/cball1990/cookbook-milestone/blob/master/wireframe.png)
    1. [Database schema](https://github.com/cball1990/cookbook-milestone/blob/master/database-schema.md)



### Features  

    * Fully Responsive 
    * The ability to add, edit, and deleted recipes
    * User login functionality

#### Existing Features  

The main features of the app is the ability to add, edit, delete and look up recipes.  
Once you log into the app the main page has all the recipes displayed, you can sort  
the recipes by name or the amount of upvotes it has. Each recipe displayed also  
has a button that allows you to view more detailed information on the recipe,  
a button to edit the recipe and one to delete the recipe. When you go and view  
more inormation on the recipe there is also a feature that allows you to upvote  
the recipe by clicking a button. On the main page of the app I added a nav bar with  
only 2 links for home and for the add recipe feature, this take you to a form that  
allows you to add details for a recipe along with basic instructions on how to fill  
the form out.

#### Features for the future

A good feature that could be added is the ability to save recipes to your own recipes  
section under a my account page, this would allow people  to save their favourite recipes  
and not have to search through all the recipes to find the one they want again.  
Another feature that could be added is to only allow the person who published the recipe  
to edit or delete the recipe, this would stop people from deleteing everything.  
The third feature I would add in the future is when you view a recipe, you would  
be able to click a button that creates a shopping list of ingrediants for you.  

### Technologies Used  

  
+ [Bootstrap](https://getbootstrap.com/)
    - Used to simplify making the app responsive and other small bits of css
    such as floats and border rounding.  
+ [Google Fonts](https://fonts.google.com/)
    - Used to find fonts to use for the text on the webpage.    
+ [HTML](https://html.com/)
    - Used to create content on the webpage.  
+ Python  
    - Python was used for all of the backend code.  
+ Flask
    - Flask was used for all the templating and routing of the project aswell as talking to the database.  
+ Mongodb  
    - Mongodb was the database I used to hold all the information on the recipes etc.  

## Testing  

To test my app I mainly used manual testing, this involved looking at every form to check  
if i could enter the wrong information in the fields, for example, a list of numbers into  
a url field, this ensures that users can only enter the required information into an input,  
to test the forms further I also went through and filled in forms with missing fields to see  
if they would validate with missing information, I also checked the responsiveness of all the  
pages down to a minimum width of 347 pixels as the smallest mobile screens are around 355 pixels in width. 
To do this I used chrome dev tools and different devices I own to view the app on differnt browsers and devices.   
To help me test the app i asked friends to use the app and give me feedback on any issues they encountered,  
this helped me catch some bugs I hadn't noticed, for example when you updated the recipes it would  
reset the upvotes count back to 1. I also used online code validators to validate my html, css and  
python code, (see the python validated.png for the confirmation of validated code).  

### Testing User Stories    
     * First Time Visitor Goals
        1. As a first time user I should be able to signup and login easily.
            * upon entering the app the user is greeted with a login / signup page
        1. A first time user should be able to navigate the app without confusion.
            * the navigation bar is always at the top of the page with no extra links then what it needs
        1. As a first time visitor to the app I should be able to see my saved recipes instantly
        so i can reference them as I cook
            * Upon logging in the the app all recipes are displayed on the home page with the abilty to click on them to see more details

    * Returning Visitor Goals
        1. Returning users must be able to edit and update saved recipes to make adjustments to the recipes
            * every recipe can be edited or deleted easily with a button under each recipe
        1. As a returning user I should be able to delete recipes I didn't like
            * Each recipe has a delete button next to it
        1. As a returning visitor I am able to add new recipes through a form quickly
            * the Nav bar has an add recipe link that takes you to the add recipe form.
            
### Known Bugs 
    * The edit and delete button on the home page over lap slighty just before the mobile break point

## Deployment  

To deploy this app I used Herouku. To do this I had to add a requirements.txt file and  
a Procfile in order for heroku to be able to run the code and get it deployed. When you first visit the  
app you are required to log in to view the recipes and to make changes. To run the app within the IDE you  
need to  type in the terminal- python app.py .  

## Credits 

#### Media  

+ Page Logo - Taken from [www.thelogomix.com](http://www.thelogomix.com/files/imagecache/v3-logo-detail/cookbook6-06.png) and edited to be the right colour.