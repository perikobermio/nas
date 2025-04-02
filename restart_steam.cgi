#!/bin/bash

#steam steam://open/bigpicture
echo "Content-type: application/json"
echo ""
cat <<EOF
{
  "message": "Hello, CGI World!",
  "status": "success",
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
