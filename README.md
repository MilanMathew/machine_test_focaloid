## Solutions of Machine Test
This code has been tested to work on python3. Answers of the first two questions are given in the 'solutions' directory. For demo, web app is hosted at [heroku](https://stats-pl.herokuapp.com).  
To run the flask web app locally, you will need docker and docker-compose installed on your system. Then run these commands in the project directory:  


    docker-compose -f docker-compose.yml up  
Open new terminal and run:  


    docker exec -it focaloid flask db upgrade  

Now the app will be running at [localhost](localhost:5000).      
### Unittests
To run unittests on the focaloid container, make sure the container is running then open a terminal and run:  


    docker exec -it focaloid python3 tests.py -v