<!DOCTYPE html>
<html lang="eu">
    <head>
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no, minimal-ui">
        <link href="/externos/font-roboto.css" rel="stylesheet">
        <link href="/css/app.css" rel="stylesheet">
    </head>
    <body>
        <index id="index"></index>
        @vite('resources/js/app.js')
    </body>
</html>

