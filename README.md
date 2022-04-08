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