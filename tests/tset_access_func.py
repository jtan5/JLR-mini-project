import pytest
import pymysql
from pymysql.constants import CLIENT
import pymysql.cursors

from dotenv import load_dotenv
from source import access_func as af




def drop_database_if_exists(db):
    with af.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {db}")


def show_databases():
    with af.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            return cursor.fetchall()


def create_customer_table():
    with af.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS customers(
                customer_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                customer_name VARCHAR(50) NOT NULL DEFAULT 'Somebody',
                customer_address VARCHAR(20) NULL,
                customer_postcode VARCHAR(20) NULL,
                servicing_area VARCHAR(50) NOT NULL,
                `availability` TINYINT NULL
                )"""
            )


def show_tables(db):
    with af.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SHOW TABLES in {db}")
            return cursor.fetchall()



def create_database(db):
    with af.create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE {db}")


@pytest.fixture(scope="module", autouse=True)
def database_fixture():
    db = "test_db"
    drop_database_if_exists(db)
    create_database(db)
    create_customer_table()

    yield db

    drop_database_if_exists(db)


def test_check_database_exists():
    # assert
    databases = show_databases()
    print(databases)
    assert {"Database": "test_db"} in databases


def test_check_table_exists():
    tables = show_tables("test_db")
    print(tables)
    assert {"Tables_in_test_db": "customer"} in tables


def test_insert_into_customer_table():
    # assemble
    db = "test_db"

    # act
    af.insert_customer("DummyName", "DummyAddress", "DummyPostcode", "DummyServicing_area")
    expected = {"customer_name":"DummyName", "customer_address":"DummyAddress", "customer_postcode":"DummyPostcode", "servicing_area":"DummyServicing_area"}
    # assert
    customers = af.import_customer_db()
    assert expected in customers