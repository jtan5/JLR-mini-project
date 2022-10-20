
# JLR DATA ENGINEERING BOOTCAMP CAFE - MINI PROJECT by JON TAN
##

## What is this and how should it be used?
When activated, this program will allow the user to use a python command line interface to insert new orders, products, customers and couriers into the mySQL database. The mySQL database is assumed to be running on the same machine that the user is using the python interface with.

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
Type the following in the bash terminal:

```bash
make install
```
## Usage
Type the following command in the bash terminal to run it:

```bash
make run
```
## I can't connect to the mySQL database, what should i do?
No don't ring 015 yet... first run these 2 commands in your bash terminal line by line.
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