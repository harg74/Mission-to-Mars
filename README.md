# Mission-to-Mars

## Overview

The purpose of this project was to aquire the ability to extract information from the NASA Science Mars Exploration website using Chrome Developer, Beautiful Soup & Splinter. With Splinter, we were able to automate our web browser and perform the scrape. On the other hand, we also used MongoDB to store the retrieved data and finally we used Flask to create a web application to display the following data:

- Latest News
- Featured Image
- Facts about the planet
- Images of the hemispheres

## Results

1. We began by creating our first script in Jupyter Notebooks, called Mission_to_Mars_Challenge.ipynb. Which was utilized to begin our scrape task and get the requested information we needed to build our app. The script includes the usage of ```Splinter``` and ```BeautifulSoup``` to automate the browser and parse the retreived HTML elements.<img width="1239" alt="html" src="https://user-images.githubusercontent.com/78564912/143180736-de5c4326-0f0b-4344-b8c0-60fefbe5622d.png">


---> See full code here:

![CodeB S](https://user-images.githubusercontent.com/78564912/143177660-ce08ecb6-264d-4d23-90ef-d33aa4172523.png)

2. Our next step was to convert our file Mission_to_Mars_Challenge from .ipynb to .py and edited it in ```Visual Studio Code```, where we added functions to follow the DRY principle, to scrape through the required webpages, retreive the HTML elements and store them in ```MongoDB```.

    This time we updated our scraping.py code with Mars Hemispheres using the database in Mongo. In addition to this, we created a ```Flask``` app to display in a       beautiful and meaningful way, the retreived data and created our app routes. These routes help to display the information on the home page and will perform the     scraping of new data using the codes that we wrote in the Python script.
    
    ![image](https://user-images.githubusercontent.com/78564912/143179239-61829e58-fa40-4340-b66e-ce6a0c583be8.png)
    
    Finally, we created an HTML template to customize the the web app and use Bootstrap components to make prettier the HTML and CSS the file.
    
    <img width="1239" alt="html" src="https://user-images.githubusercontent.com/78564912/143180777-11c48c87-bf99-453a-8169-b3ee50a229a4.png">

---> See full code here:


3. As an additional update to our web app, we changed the color of the jumbotron element, update the background color to make it look more *'martian'* and re-arrenged the Mars Hemispheres images as thumbnails. Also, was very important that our web was responsive regardless the viewport.

---> See full code here:

![Screen Shot 2021-11-23 at 21 56 53](https://user-images.githubusercontent.com/78564912/143181035-a1a503b2-16da-430e-9fd3-44ef6afeca8f.png)

![Screen Shot 2021-11-23 at 21 57 04](https://user-images.githubusercontent.com/78564912/143181045-d6b13362-f62c-48ee-891e-1aba2e6439a0.png)

![image](https://user-images.githubusercontent.com/78564912/143181453-d11b8dbd-71a6-4339-a286-2dc3a5491ca5.png)


