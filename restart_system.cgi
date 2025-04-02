#!/bin/bash

#steam steam://open/bigpicture

reboot

echo "Content-type: application/json"
echo ""
cat <<EOF
{
  "message": "SYSTEM restarted",
  "status": "success",
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
