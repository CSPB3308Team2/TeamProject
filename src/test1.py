#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest.case import TestCase
from unittest.loader import TestLoader
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import unittest
import main
import sqlite3
import json
import time
# from threading import Thread


class todos_TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # if __name__ == "__main__":
        #     Thread(target=main.app.run(debug=True)).start()
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):

        # storedb.create('db.sqlite')
        # storedb.fill('test.db')
        pass

    def tearDown(self):
        # os.remove('test.db')
        pass

    # Test correct userid, should match with rowid, making sure add fcn is working, only works for fresh db before deleting
    def test_correct_rowid(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()
        test = cursor.execute(
            """SELECT id FROM todo ORDER BY id DESC LIMIT 1""")  # get last id
        myresult = cursor.fetchall()
        expected = cursor.execute(
            """SELECT max(id) FROM todo""")  # get last rowid
        myexpected = cursor.fetchall()
        if len(myresult) > 0:
            result = [i[0] for i in myresult]  # parse character
            result = str(result)[1:-1]
            result = int(result)
            expect = [i[0] for i in myexpected]  # parse character
            expect = str(expect)[1:-1]
            expected = int(expect)
            # print(result)
            # print(expect)
            #expected = 3
            self.assertEqual(result, expected, "Does not match")

    def test_add(self):
        # form the request data

        hammertime = {"title": "buy a hammer", "place-name": "hammers r us", "place-address": "123 hammer way",
                      "traffic-data": "[]"}

        requests.post('http://127.0.0.1:5000/add', data=hammertime)

        # '[[0,0,0,45,65,75,80,80,70,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,65,80,65,60,70,75,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,50,65,70,65,70,85,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,50,60,55,55,75,100,95,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,70,90,85,75,70,70,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]'

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        # print(cursor.execute("""SELECT * FROM Todo""").fetchall())

        test = cursor.execute(
            """SELECT title, place_name, place_address, traffic_data FROM Todo WHERE title='buy a hammer'""").fetchone()

        self.assertEqual(test, ('buy a hammer', 'hammers r us', '123 hammer way',
                         '[]'), "error: hammertime didn't happen")

        obj = cursor.execute(
            """SELECT * FROM Todo WHERE title = 'buy a hammer'""").fetchone()
        # print(obj)
        id = obj[0]

        # make the delete request with the url appended with the id
        requests.get("http://127.0.0.1:5000/delete/{}".format(id))

        test = cursor.execute(
            """SELECT title, place_name, place_address, traffic_data FROM Todo WHERE title IN ('buy a hammer')""").fetchone()

        self.assertEqual(test, None)

        conn.close()

    def test_delete(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        test = cursor.execute(
            """SELECT title, place_name, place_address, traffic_data FROM Todo WHERE title='plant a garden'""").fetchone()

        # self.assertEqual(test, None, "garden time already exists in database")

        gardentime = {"title": "plant a garden", "place-name": "green thumbs", "place-address": "456 rose bush",
                      "traffic-data": "[]"}

        requests.post('http://127.0.0.1:5000/add', data=gardentime)

        test = cursor.execute(
            """SELECT title, place_name, place_address, traffic_data FROM Todo WHERE title='plant a garden'""").fetchone()

        self.assertEqual(test, ('plant a garden', 'green thumbs', '456 rose bush',
                         '[]'), "error: garden time didn't get added to database")

        # get the id of garden time

        obj = cursor.execute(
            """SELECT * FROM Todo WHERE title = 'plant a garden'""").fetchone()

        id = obj[0]

        # make the delete request with the url appended with the id
        requests.get("http://127.0.0.1:5000/delete/{}".format(id))

        test = cursor.execute(
            """SELECT title, place_name, place_address, traffic_data FROM Todo WHERE title='plant a garden'""").fetchone()

        # print(cursor.execute(
        #     """SELECT * FROM Todo""").fetchall())

        self.assertEqual(test, None, 'garden time never ended')

        conn.close()

    def test_update(self):
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        doitnow = {"title": "do it now", "place-name": "here", "place-address": "the choppa",
                   "traffic-data": "[]"}

        requests.post("http://127.0.0.1:5000/add", data=doitnow)

        obj = cursor.execute(
            """SELECT * FROM Todo WHERE title = 'do it now'""").fetchone()

        orig = obj[-1]
        obj_id = obj[0]

        requests.post("http://127.0.0.1:5000/update/{}".format(obj_id))

        test = cursor.execute(
            """SELECT * FROM Todo WHERE title = 'do it now'""").fetchone()[-1]

        self.assertEqual(bool(test), bool(orig),
                         "error: you procrastinated")

        requests.get("http://127.0.0.1:5000/delete/{}".format(obj_id))

        conn.close()

    def test_about(self):
        tester = requests.get('http://127.0.0.1:5000/about')
        # print(tester)
        # print(tester.status_code)
        self.assertEqual(tester.status_code, 200,
                         "error: response didn't work")

    def test_root(self):
        tester = requests.get('http://127.0.0.1:5000/')
        # print(tester.status_code)
        self.assertEqual(tester.status_code, 200,
                         "error: root didn't work")

    def test_home(self):
        tester = requests.get('http://127.0.0.1:5000/home')
        # print(tester.status_code)
        self.assertEqual(tester.status_code, 200,
                         "error: root didn't work")


        # Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
