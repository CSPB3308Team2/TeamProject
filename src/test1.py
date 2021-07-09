#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import unittest
from main import app
import sqlite3


#app = Flask(__name__, static_folder="static")

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbtest.sqlite'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)

class todos_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        #storedb.create('db.sqlite')
        #storedb.fill('test.db')
        pass

    def tearDown(self):
        #os.remove('test.db')
        pass

    # Test correct userid, should match with rowid, making sure add fcn is working, only works for fresh db before deleting
    def test_correct_rowid(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        test = cursor.execute("""SELECT id FROM todo ORDER BY id DESC LIMIT 1""") ##get last id
        myresult = cursor.fetchall()
        expected = cursor.execute("""SELECT max(id) FROM todo""") ##get last rowid
        myexpected = cursor.fetchall()
        result = [i[0] for i in myresult] ##parse character
        result = str(result)[1:-1]
        result = int(result)
        expect = [i[0] for i in myexpected] ##parse character
        expect = str(expect)[1:-1]
        expected = int(expect)
        #print(result)
        #print(expect)
        #expected = 3
        self.assertEqual(result, expected, "Does not match")

    #def test_add(self):
        #conn = sqlite3.connect('db.sqlite')
        #cursor = conn.cursor()
        #test = cursor.execute("""SELECT title FROM todo""")
        #myresult = cursor.fetchall()
        #expected = "pizza"
        #print(myresult)
        #result = self.app.post('/add', data=dict(title=='Coffee', place_name='All Star Cafe'), follow_redirects=True)
        #self.app.post('/add', data=dict(var1='data1', var2='data2', ...))
        #self.app.get('/path-to-request', query_string=dict(arg1='data1', arg2='data2', ...))
        #self.assertIn(expected, myresult)

    def test_index(self):
        #with app.test_client() as client:
            #self.app.post('/add', data = dict(title= 'Coffee'))
            #tester = app.test_client(self)
            #response = tester.get("/add")
            #statuscode = response.status_code
            #self.assertEqual(statuscode, 200)
        tester = app.test_client(self)
        response = tester.get("/about")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


		# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
