
![General Assembly's Logo](https://camo.githubusercontent.com/603ef5eae7d28900a9678ae96c6c60a9c72f8a059c328b28cf978df999cea1f8/68747470733a2f2f692e696d6775722e636f6d2f6c7a56493364382e706e67)

# The Phonograph - A Collection of Records

## Goal

Inspired by Discogs.com, the full-stack record collection app was built in 4 days on a Django Framework, connected to a PostgreSQL database which utilised vanilla CSS, Tailwind and JavaScript to style its front-end. Users can navigate the site as a guest, the site displays a collection of records and artists, these are all user uploaded. Registered users have upload, delete and edit privileges.


## The Landing Page
![App home page screenshot](/thephonograph/main_app/static/images/Homepage%20Screenshot.png)
## Record Details Page
![Record detail page screenshot](/thephonograph/main_app/static/images/Record%20Detail%20Screenshot.png)


### Technical Requirements Satisfied
- The application includes at least 2 related models, one of them being the User, and the major CRUD functions have been implemented.
- Some pages have a restricted access, therefore they can only be viewed by logged-in Users, the User is also able to sign-up/login, change the password and logout.
- The Users receives feedback messages for success/fail form submissions, some of the forms have mandatory fields otherwise the User is not allowed to submit them; after every submission the forms are cleared of the data.

### Technologies Used
- Git/GitHub
- HTML
- CSS
- Tailwind CSS Library
- Python
- Django
- PostgreSQL
- pgAdmin 4

### Team Members
- Elisabetta Maspero - [GitHub](https://github.com/emaspero) | [LinkedIn](https://www.linkedin.com/in/elisabetta-maspero-990bb3111/)
- Christopher Carey - [GitHub](https://github.com/christopher-k-c) | [LinkedIn](https://www.linkedin.com/in/chriskcarey/)
- Sam Hackwood - [GitHub](https://github.com/samhackwood) | [LinkedIn](https://www.linkedin.com/in/samuel-hackwood-40b050233/)


### Contribution Examples

We started off pair programming the fundamental elements of the project and later moved onto solo programming.

### Pair programming 

- Wrote the basic structure of the project together
- TrackList Model Functionality built together
- Created the record model and basic styling for the html pages

### Solo Programming

- The Artist Model and its full CRUD operations
- Styling across the site from Landing page to Records detail, including Artist grid layout and more
- Alert Messages with Bootstrap for Artist and Record CRUD, signup and more
- Carousel


### Carousel Example

- This block of code is from a tutorial I followed that produces an image carousel on our landing page. The javascript works as follows, we first assign the variable slides using querySelectorAll to each div element with the class slide. There are three html elements with a class of slide and inside each slide element there's an image tag.

- Because the slides variable is an array of three html elements I can use a forEach loop to iterate over the array. For each iteration we are setting transform property translateX, a css function, to the sum of the current slides index value multiplied by 100% and then repeating until each element within the slides array has been set a translateX percentage value.

- Arrays use zero-based indexing, so the first index is 0, the second is 1 and the third is 2. So, 0 x 100 = 0 which means the first element in the array has its translateX set to 0, the second element is set to 100 and the third element is set to 200. This now places the items on a horizontal plane, they should now be bleeding out of the right hand-side of the slide container. I will use the css property overflow: hidden; to hide this overflowing.

- Now we assign the next button to a variable called nextSlide and we also set a variable called curSlide which will keep track of the current slide. We also assign the variable maxSlide, to the maximum number of slides possible. Variables, curSlide and maxSlide allow us to keep track of the current image being displayed, if the current images index value is strictly equal to the maximum number of slides i.e. 2, then we reset the curSlide to be the first index element in the array, 0. Else, if curSlide is less than the length, 0 or 1, then add 1 to the curSlide variable.

- Lastly, for each image we move the slide by -100% every-time the button is clicked by setting `translateX(${100 * (indx - curSlide)}%;`. When the pages loads, The translateX values start as follows, slide zero is set to 0%, slide one as 100% and slide two as 200%. The first click sets slide zero to -100%, slide one is set to 0% and slide two is set to 100%. The second click sets slide zero to -200%, slide one to -100% and slide two too 0%. The last click initiates the conditional that checks curSlide with maxSlide too true, returning the first image to 0%, second to 100% and third to 200%.

- We do the same as above for the previous button but it's just the reverse.

![Carousel](/thephonograph/main_app/static/images/carousel.jpg)


### Messaging Example

- One of my contributions to this project was the user messaging, below is an example of the code that will display successful or unsuccessful alerts when logging in.
- However, It is my understanding that I have incorrectly implemented it. In this instance I have hardcoded the type of alert to the class rather than using the **{{message.tags}}** which has access to the following tags **debug, info, success, warning** and **error**. In the future I will refactor this code to be dynamic.

![Messaging](/thephonograph/main_app/static/images/messaging_01.png)

- This piece can be found inside the base.html template which is a HTML skeleton document that is replicated across the site on every page but only written once, it contains various elements, the most important of which, are the Navigation and footer bars - saving us from having to re-write these ubiquitous elements for every page on our site.

![Messaging](/thephonograph/main_app/static/images/messaging_03.png)

- This last bit of javascript removes the alert messages after 3 seconds using the setTimeout method. Inside the method i am targeting the id of the alert html element which is created when the alert is triggered. I then set that html element to a display of none which hides the element from the page.

![Messaging](/thephonograph/main_app/static/images/messaging_02.png)

> Messaging Visual Example

![Sign_up_messaging](/thephonograph/main_app/static/images/sign_up_image.gif)


### Process

##### Day 1
As a first step we started laying out the several connections using ERDs as that helped us to determine which Models were going to be part of the application and how they would interact with each other. We proceeded with creating a Trello board and assigning tasks to each member of the Team and, subsequently, using Figma we created a basic layout on how we would like the application to look like.

The focus for the first day was mainly to create the starting code for this project, creating our first two Models (Record and Track-list) and adding the User auth functionality. At the end of the day, the User was able to sign-up, login and create/update/delete a Record and while in the record detail page the User was also able to add tracks to that specific record's track-list.


###### Trello
![Trello board screenshot picture](/thephonograph/main_app/static/images/Trello%20Screenshot.png)
[Trello Board](https://trello.com/b/NnHgZg5d/project-03)
###### ERD (Entity Relationship Diagrams)
![ERDs screenshot](/thephonograph/main_app/static/images/ERDs%20Screenshot.png)
###### Wireframes
![Figma screenshot](/thephonograph/main_app/static/images/Figma%20Screenshot.png)
###### User Stories
![User Stories](/thephonograph/main_app/static/images/User%20Stories.png)

##### Day 2
During the second day, part of the time was dedicate to edit the sign-up form allowing the User to also input first name, last name and email address alongside the standard username and password. The functionality to allow the User to reset the password was also implemented. Two additional Models were created (Artist and Crate). The User was now allowed to add the favourite Records to its own Crate. The links-display has been amended, now a logged-in User can see and access several more pages compared to a non-logged-in User.

##### Day 3
Several bugs were fixed during the third day, starting from the one that was preventing the Artist's name to show up on the Record's detail page. We have added the functionality to clear a form after submission and the feedback messages after success/fail form submission were now fully functioning.

During the afternoon part of the Team started working on the styling for the application and the other part of the time started working on the readme file.


##### Day 4
The Team has been focusing mainly on the styling using Tailwind CSS Library and deploying the app on Heroku.

### Deployed application link

[The Phonograph](https://hydro-keener-88414.herokuapp.com/)

### Challenges

As a team we found it challenging to fully understand what happens in the background with the CBVs, as the code is a lot shorter and less obvious than express, it's not always immediately clear what the issue is. 

We struggled to understand how to pull data from models that were linked by relationships and show it on the page (eg. how to display the Artist name from the Record page considering that the relationship was many too many). In the end we realised that the Artist was stored as an array, which was why simple dot notation failed to yield a result, therefore we needed to employ a for loop in the form of backend Django programming, this would give us the Artist in the Records detail page.

We decided to implement Tailwind CSS Library, which we did not have experience with and does take time to understand to make full use of the features that it offers. In the future I will hold off from implementing a framework or library that I do not have experience with, when the timeline for the project is so strict.

When debugging we ran a vast number of Google searches and the answers that we got were not always the easiest to understand or implement due to the variety of ways in which developers work, especially based on their experience.


### Features to be added in the future

- The password reset email only gets sent to the Terminal at the moment, the link fully works and the functionality fully works, but it would be good to have it as an actual sent email instead. We could also implement a verification email to be sent upon registration of a new User.
- Implement on the homepage, a carousel showing the latest record that has been added to the database.
- Different levels of privileges based on the User type.
- User profile page.
- Make the app fully responsive.
- Install Tailwind with the config file, rather than just import it via the link, to fully explore how to personalise it.
- Embed Youtube video related to Artist/Record on the detail pages.
- Utilise a third party API, in this case Discogs API and include pagination.
- Create a Label model that behaves in a similar way to the Artist model.

### Key Learnings & Wins

- Enhanced my understanding of Django Framework and relational databases i.e. PostgreSQL.
- Experience reading Documentation and implementing functionality based on that research.
- Template extending is a great way to write something once but render as much as you like, this was something we were quick to implement.
- Unlike in MongoDB, we were required to manually migrate major changes to the database in PostgreSQL, this was something that as a team we had to keep a watchful eye on.
- Class Based Views took some time for me to get my head around.
- We would have benefited from more research at the beginning of the project into a Tailwind CSS framework, which if installed using the Tailwind CLI would have been customizable and production ready, however we used Tailwind Play CDN which is only for development purposes and was a decision made due to time constraints.


### Bugs 

- The application is not fully responsive, in the future i would like to make it fully responsive but by using the Tailwind CSS framework. 
- The crate is broken, when trying to view, create and add to the create.


