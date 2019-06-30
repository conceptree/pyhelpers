#!/bin/bash

from selenium import webdriver

browser = webdriver.Chrome('./assets/webdrivers/chromedriver')
browser.get('http://www.conceptree.com');