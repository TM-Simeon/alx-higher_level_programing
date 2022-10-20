#!/bin/bash
# find the lenth of a url
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
