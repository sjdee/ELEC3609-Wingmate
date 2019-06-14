# Wingmate

Find mates, get dates!

Live at: http://ec2-13-55-94-224.ap-southeast-2.compute.amazonaws.com/

## To Run ##

Standalone
```sudo ./run.sh```

Service
```sudo systemctl start wingmate```

## Prerequisites

### Python ###

```sudo apt install python```
```sudo apt install python-pip```


### Create and deploy virtual env ###

```sudo apt install virtualenv```

```virtualenv wingmate_env```

## Virtual Env Method

Source with ```source wingmate_env/bin/activate```

### Download dependencies ###

```sudo pip install -r requirements.txt ```

To resolve GDAL dependencies on

#### OSX
```brew install GDAL```

#### Linux

```sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable```

```sudo apt-get update```

```sudo apt-get install python-gdal```

```sudo apt-get -f install1```

```sudo apt-get install python-gdal```

```apt install spatialite-bin```

```sudo apt-get install libsqlite3-mod-spatialite```

``` sudo apt-get install libsqlite3-dev```
## Data Models

### Chatroom ###
#### Message ####
This model is used for sending data between chat users.
It consists of a message, a sender and a specific chatroom.

#### Chatroom ####
This model is used for representing an individual chatroom between two users.
It consists of two bounded users, user1 and user2

### WingMap ###
#### WingManLocation ####
This model keeps track of any given wingmans location.
It consists of the name of the wingman and a GPS coordinate.

### SiteWide ###

#### User ####
This is a default django model that is used for storing User details.
It consists of a

*  username

*  first name

*  last name

*  email

*  password

*  group

*  user permissions

*  admin permission

*  active state

*  super user state

*  last login time

*  date joined time

#### WingmanUser ####
This model stores all details for  user.
It extends the default user class in django.

