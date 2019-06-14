# DOCUMENTATION

To the beneficiary, this document is based around Mac users and some of the commands given below might only work for the specified environment. This guide will run you through each step; from setting up an environment after you've downladed the code base on your local machine, to using the service and making you familar with the interface.

From the user's perspective, The guide runs through how the different pages are linked together, what functionality does each page provide and what priviliges does he/she have while using it. Also, in this section we briefly talk about which library makes it possible to achieve that functionality. 

From the coder's perspective, This guide also talks about how different files are setup in the backend, their hierarchy and what the architecture of the code is like.


## SETTING UP FILES 

This section assumes that `python`, `pip` and `virtualenv` is already installed on you local machine. 
If not, check APPENDIX at the bottom of this file.

1. Download Code Base

	Once you've downloaded the code base and put in ``` <your-directory> ``` one can move to the next step
	
2. Set up Virtual Environment
	
	While being in ``` <your-directory> ```, run the command ```virtualenv wingmate_env``` to make a virtual environment for your project. The benefit of this is that the packages and libraries we install just for purpose of the project, will not hinder with the files and packages on your local machines and their scope would be limited. 

3. Install required packages

	Once the virtual environment is setup, it's time to activate the virtual environment using the command ```source wingmate_env/bin/activate``` and install the required packages.

	A list of all the required packages is provided in the requirements.txt file and the following command will install all the packages at once. If you do encouter any error, a list of common errors and the way to go about them is provided in the appendix.
	
	```pip install -r requirements.txt ```
	
4. Run the server

	Once the virtual environment is setup and all the packages are installed the development server available in django may be fired using the command ```python manage.py runserver ```.

	For your convenience, a run.sh file is provided as an alternative to this step. And if it is ran, then this step may be skipped.


## For the User
<--How the user will navigate between pages>


## For the Coder

**The Wingmate project has multiple applications serving different purposes across the website. **
The applications namely being: **SignUp, MyApp, WingMap, ChatBox and Premium. **

Each of these applications have a detailed Readme.md in their respective folders talking about their functioning. 
Here, we briefly cover the important features.

* Signup

* MyApp

* WingMap

* ChatBox

* Premium


<-- How the pages work>
* templates
* views

<-- Bower components>


# APPENDIX

## COMMON ERRORS

* SERVER ERROR WHEN LOGGING IN! "The pysqlite library does not support C extension loading."
	
	Go to the root folder of your project with the virtual environment activated and run the follwoing commands:

	```
	brew update
	
	brew install sqlite  # 3.8.5
	
	brew install libspatialite  # 4.2.0
	
	brew install spatialite-tools  # 4.1.1 
	
	git clone https://github.com/ghaering/pysqlite.git
	
	cd pysqlite 
	```
		
	Make sure the versions are up to date! 
	
	**Next:** Modify the setup.cfg file to look like and save it:
	
	```
	[build_ext]
	
	libraries=sqlite3
	
	include_dirs=/usr/local/opt/sqlite/include
	
	library_dirs=/usr/local/opt/sqlite/lib
		
	# define=SQLITE_OMIT_LOAD_EXTENSION	
	```

	**Next:**
	
	``` 
	python setup.py build
	
	python setup.py install	
	```

* six 1.4.1 installation issue: "OSError: Not Permitted" 
	
	Remove six 1.4.1 from requirements.txt and run the file again

* Bad magic number fix: 
	
	delete all generated myapp/*.pyc files

* Install Postgresql
	
	```brew install postgresql```

* Postgresql error: role "geodjango" does not exist
	
	```createuser --superuser geodjango```

* Postgresql error: database "geodjango" does not exist
	
	```createdb geodjango```

* Postgresql error: could not connect to server, connection refused
	
	```pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start```

* Install all the required packages
	
	```pip3 install -r required_packages.txt```