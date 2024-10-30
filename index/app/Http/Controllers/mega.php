<?php
namespace App\Http\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\File;


class Mega extends Controller
{
	public function get(Request $request) {
		$megas = json_decode(File::get(storage_path('mega_download_urls.json')), true);
		return $megas['downloads'];
	}

	public function set(Request $request) {
		//$megas = json_decode(File::get(storage_path('mega_download_urls.json')), true);
		return $request->all();
	}
}
