> ## ![Tux, the Linux mascot](https://1nfluencersmarketing.com/wp-content/uploads/2020/01/1n-logo-black-uai-258x31.png)
### Back End Test
### <center>Theoretical Test</center>
1. How does one combine two Pandas dataframes?
    > According to official documentation: Merge, join, concatenate and compare.
In this application I used append(), deprecated since version 1.4.0
2. What is the difference between a local variable and a global variable?
   > Global variable is the one that we declare in the main scope of the application and the local variable is the one that is declared inside a function outside the main scope of the program.
3. How does one create a copy of a dataframe using Pandas?
    > We can perform the copy using the copy() command.
Ex: my_data_frame = pandas.DataFrame(data) -> 
   > new_data_frame = my_data_frame.copy()
4. How does one handle concurrent requests in Flask?
    > Flask does not manage the threads, this function is used by Gunicorn to perform the application.
When running the app we pass the parameters.
Ex: gunicorn --workers=5 --threads=2 app:app
5. What is a Replica Set in MongoDB?
    > It is a way of replicating several database datasets as a form of security and not for a service. And we can use these dataset sets to perform readings by different users at the same time.
These sets work as follows.
Ex: dataset_primary, dataset_secondary01 and dataset_secondary02.
Only the primary receives writings, everyone receives readings, when they write to the primary, it replicates to all the secondaries and if the primary falls, a secondary assumes as primary and starts to receive the writings;
6. What is a Transaction in a database context?
    > In an abstract and simplified way, a transaction
can be seen as a set of
data read and write operations.
These transactions have their priorities.
Ex: 
   > – Atomicity 
   > – Consistency
   > – Isolation
   > – Durability or Persistence

## Practical Test
* Create an application using Python, Flask and SQL to register and authenticate an user.
The user must have an unique email address and the password must have at least 8
characters.
* The application must consult an external API, such as PokeAPI(https://pokeapi.co/), use
Pandas to process the data and save it in a MongoDB database. The CRUD endpoints
for this part of the application must be accessible only to a previously authenticated user
existing in the SQL database. All endpoints must return an JSON response with status,
data, message and HTTP code.
* The project must be added to a public repository on Github and shared with the person
responsible for the selection. The README.md file must contain the answers for the
theoretical test, as well as the instructions necessary to execute the project.
The code must be well documented and follow good development practices.

--------------------------------------------------------------------------
> ### Starting
This application performs user authentication using MongoDB.
It allows registering the user and changing the password.
The user logging in has access to Pokemon research using the api (https://pokeapi.co/) we consume this api and treat the data using dataframes (Pandas) and finally registering in mongoDb with the pokemon's name, photo of the pokemon and its ability.
And we display a table of registered pokemon.
When we make the query in the api, it presents the information handled with Pandas in JSON format.

#### Class used:
   * driver_mongodb -> Contains the connection string with mongoDB.
   * poke -> Class that receives the dataframe parameters with their respective getter and setter.
   This class is a master class.
   * poke_abilities -> Extend class Poke for PokeAbilities
   one for many, one Pokemon for many abilities.
   This class inherits the name and photo attributes from the master class.
   This class returns a dictionary.
   * user -> User class where it receives the parameters email, name and password.
The getter and setter was generated and has a dictionary return.

#### Method used:

* poke_delete -> takes as a parameter the Poke class.
* poke_select -> Method for select pokemon in mongoDb
  1. The first function takes the name of the pokemon to query and returns a dictionary
  2. The second function receives or does not receive attributes, it queries all pokemon registered in mongoDB and returns a pandas.DataFrame
* poke_insert -> Method for insert pokemon in mongoDb
takes as a parameter the Poke class
perform the query to check if you already have the registration.
* poke_update -> Method for update pokemon in mongoDb
takes as a parameter the Poke class for update in mongoDb
* poke_df -> Method for process DataFrame in Pandas
This function receives the name of the pokemon as a parameter and performs the query in the API.
A dataFrame was created to receive the JSON from the API query.
A loop was created to check the pokemon's skills, as it has pokemon with more than one skills.
In the loop I compare the dataFrames and pass skills and other information to the Poke Class which returns me a dictionary ready to send to mongoDB.
this return a json classification for records
* users_delete -> Function to delete user in mongoDB is passed as a parameter to the Users class
* users_insert -> Function to insert user in mongoDB is passed as a parameter to the Users class
Perform the query before inserting
* users_select -> Function to select user in mongoDB
  1. This function receives as a parameter the email to perform the query
  2. This function receives the email and password as a parameter to perform the query and authenticate by sequence.
  3. Both functions return a dictionary
* user_update -> Function to update user in mongoDB is passed as a parameter to the Users class

> ### How to run the application
#### Use python version 3.10 up.

1. git clone https://github.com/escoobi/1nfluencersmarketing
2. pip install pandas
3. pip install flask
4. pip install -U Flask-WTF
5. Enter the repository folder.
6. run command Scripts/active
7. run flask run
8. access link
9. register a user
10. auth user
11. enjoy!