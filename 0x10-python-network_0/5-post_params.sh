#!/bin/bash
# script that sends a POST request with variables
curl -s -X POST $1 -d '{"email:test@gmail.com","subject:I will always be here for PLD"}'
