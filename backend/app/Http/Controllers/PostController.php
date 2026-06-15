<?php

namespace App\Http\Controllers;

use App\Models\Post;
use Illuminate\Http\Request;
use Illuminate\Validation\Rule;

class PostController extends Controller
{
   
    public function index(Request $request)
    {
        $validated = $request->validate([
            'classification' => ['nullable', Rule::in(['information', 'incident'])],
            'page' => ['nullable', 'integer', 'min:1'],
            'per_page' => ['nullable', 'integer', 'min:1', 'max:100'],
        ]);

        $perPage = $validated['per_page'] ?? 15;

        $query = Post::query()->orderByDesc('post_date');

        if (! empty($validated['classification'])) {
            $query->where('classification', $validated['classification']);
        }

        return response()->json($query->paginate($perPage));
    }
}
