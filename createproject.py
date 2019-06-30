#!/bin/bash

def createproject ():
    mkdir 'src'
    mkdir 'src/main'
    mkdir 'src/main/resourcers'
    mkdir 'src/main/resources/static'
    cd 'src/main/resources/static'
    mkdir 'assets'
    mkdir 'data'
    touch 'index.html'
    touch 'main.js'