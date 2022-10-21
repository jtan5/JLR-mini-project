
# JLR DATA ENGINEERING BOOTCAMP CAFE MINI PROJECT
## by JON TAN

## What is this and how should it be used?
When activated, this application will allow the user to use a python command line interface to insert new orders, products, customers and couriers into the mySQL database. The mySQL database is assumed to be running on the same machine that the user is using the python interface with.

In theory it would be possible to connect to a mySQL database not on the same machine, however that is not yet covered in this release.


## Pre-requisites
```
# 1 - Bash terminal (easy for mac users, good luck for windows users)
# 2 - Python 3.8  or later
# 3 - mySQL installed with a local instance of a database
# 3 - Patience of a saint cause tech support will take a significant time
```


## Installation
Installation made using using the Makefile in root folder. 

The root folder is the folder that contains the <i>app.py</i> file and contains the following folders:
<br><b>db</b> - this contains the <i>cafe_db.sql</i> script which is activated during usage. This will create the appropriate databases if they are not currently present
<br><b>data</b> - this contains <i>.csv</i> of products, couriers, customers and orders which is generated on close of application.
<br><b>source</b> - this contains all the important .py files which are essential for the smooth running of the application. Editing anything in here will void warranty and incur a <b>£400 penalty fee</b> for pulling the latest version from Github.
<br>and other folders which don't really do anything... 

If you are not in the root folder, you would have to navigate there using the <b>cd </b> command.


Type the following in the bash terminal in root folder of the application:

```bash
make install
```
If you do not wish to run the make command, you can instead type this into the bash terminal:
```bash
pip install -r requirements.txt
```


## Usage
Type the following command in the bash terminal in root folder of the application to run it:

```bash
make run
```
If you do not wish to run the make command, you can instead type this into the bash terminal in root folder of the application:
```bash
pip install -r requirements.txt
```
## I can't connect to the mySQL database, what should i do?
No don't ring 015 (IT Helpdesk) yet... first run these 2 commands in your bash terminal line by line.
```bash
echo $WSL_HOST_IP
export WSL_HOST_IP=$(awk '/nameserver/ { print $2 }' /etc/resolv.conf)
echo $WSL_HOST_IP
```
This should spit out an ip address that looks like:
188.33.55.1

Copy and paste this ip address that the terminal spits out in to file titled <b>.env</b> where it reads <b>local host=XXX.XX.XX.X</b>

## How are the databases relational
The database has been set up such that orders are children of customers / products / couriers. It is therefore not possible to remove a customer / product/ order if there is an order set up for that particular customer / product/ order. The order of the to be deleted person (eg: Liz Truss) should first be removed from the database.


## How can I test coverage?
Unit test was used to iron out the main logic and flow of the different functions, integration testing is yet to be implemented in this release.
```bash
coverage run -m pytest ./tests
```

## What's planned for future releases?
The plan is to make this more robust and fit for purpose for a volunteering organisation which is in need of a simple free database solution.

## Q&A on how does this application works
1. How does python know what the <b>order_id</b> is before mySQL assigns it?
<br><i>It assigns a random integer between the limits allowed by mySQL: -2147483648 to 2147483647</i>

2. How does it assign a courier to an order?
<br><i> It does this by randomly selection an available courier within the same servicing area</i>

3. This cafe has lots of famous people as customers, how do you get so popular?
<br><i> Hard work and going above and beyond goes a long way. :)</i>

4. There is alot of recursive functions, won't it stack overflow eventually?
<br><i> Definitely, the limit is around 999... so best to only spin up the application when you need to</i>
