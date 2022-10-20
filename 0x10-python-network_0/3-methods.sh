#!/bin/bash
# display all HTTP methods the server will accept
curl -v -X OPTIONS $1
