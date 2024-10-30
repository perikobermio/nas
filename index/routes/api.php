<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

Route::get('/mega', 'App\Http\Controllers\mega@get');
Route::post('/mega', 'App\Http\Controllers\mega@set');

