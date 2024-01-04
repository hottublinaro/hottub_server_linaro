#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import mysql.connector

class Connect_db :
    def update_setting_mode():
        mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="stws1234",
            # user="root",
            # password="root",
            database="hottub"
        )
        return mydb
        


