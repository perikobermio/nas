git add .
git commit -m "pull sh"
git push -u origin master
ssh -p 21 erik@ebu.freemyip.com "docker exec -i laravel git pull"