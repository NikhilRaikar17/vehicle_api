# Vehicles API
This is a small flask web application api which contains vehicles data. A vehicle contains basic configurations such as its name,brand,description etc.. .We can add,update or search a vehicle based on its general attributes.

## Project Structure
The Python Flask based microservices project is composed of the following: 

* [VehicleApi](#Vehicle-API)

## Vehicle-API

This services is responsible in creating an api endpoints which will help create vehicle or update a vehicle or seach a vehicle based on certain attributes present in the vehicle model.

## Database
The database used in this application is PostgreSQL.

## Source Code Structure
```
Vehicle-API
	
	|-- images                  # images of architecture and screenshots of results
	
	|-- application                  	
		|-- static
		    |-- swagger.json    # Documentation of api    
			
		|-- vehicles			# Containes Application logic with routes
			|-- entities        # Entities classes of the application
				|-- vehicle_entities.py
			|-- helpers         # Database helpers for the application
				|-- vehicle_helpers.py
			|-- service         # services of the application 
				|-- vehicle_service.py
			|-- routes.py         # routes application
		|-- models.py         		# Database models of application
	|-- config.py	
	|-- requirements.txt            # Packages needed for the application
	|-- manage.py                    # Main file which serves as a starting point for the application
```
## Setup and Configuration
To launch the application perform the following:

### Step 1.
Download the source code and cd into it
```
cd vehicle_api
```
### Step 2.
create a virtual environment
```
python -m venv venv
```
### Step 3.
Download all the packages using pip
```
pip -r install requirements.txt
```
### Step 4.
Once the packages are installed, please initialise the database
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
### Step 5.
Once the database is initialized, you can start the application
```
python manage.py runserver
```
### Step 6.
You can access all of the api documentation using the below link
```
http://localhost:5000/api or http://127.0.0.1:5000/api
```
The above command opens up a swagger ui which contains endpoints for you to test.

> Please note the application is designed keeping the use case in mind. There would be some level of changes needed if the application is to be run in production environment.
