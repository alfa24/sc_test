#!/bin/bash

if [ "$1" == "console" ]; then
  exec python ant.py
fi

exec python app.py
