<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Post extends Model
{
    /**
     * @var list<string>
     */
    protected $fillable = [
        'source_url',
        'content',
        'media',
        'page_name',
        'post_date',
        'classification',
    ];

    /**
     * @return array<string, string>
     */
    protected function casts(): array
    {
        return [
            'post_date' => 'datetime',
        ];
    }
}
