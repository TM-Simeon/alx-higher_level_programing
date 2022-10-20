#!/bin/bash
# display all HTTP methods the server will accept
curl -s -v -X OPTIONS $1
