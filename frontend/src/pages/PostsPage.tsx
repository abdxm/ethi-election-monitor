import { useCallback, useEffect, useState } from 'react'
import {
  fetchPosts,
  type Classification,
  type PaginatedPosts,
  type Post,
} from '../api/posts'
import PostCard from '../components/PostCard'
import PostModal from '../components/PostModal'

type Filter = 'all' | Classification

export default function PostsPage() {
  const [filter, setFilter] = useState<Filter>('all')
  const [page, setPage] = useState(1)
  const [result, setResult] = useState<PaginatedPosts | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [selectedPost, setSelectedPost] = useState<Post | null>(null)

  const loadPosts = useCallback(async () => {
    setLoading(true)
    setError(null)

    try {
      const classification = filter === 'all' ? null : filter
      const data = await fetchPosts(page, classification)
      setResult(data)
    } catch {
      setError('Failed to load posts. Make sure the Laravel API is running.')
      setResult(null)
    } finally {
      setLoading(false)
    }
  }, [filter, page])

  useEffect(() => {
    loadPosts()
  }, [loadPosts])

  const handleFilterChange = (next: Filter) => {
    setFilter(next)
    setPage(1)
  }

  return (
    <div className="posts-page">
      <header className="posts-header">
        <div>
          <h1>EthiElection</h1>
          <p className="subtitle">Ethiopian political Facebook posts monitor</p>
        </div>

        <div className="filters" role="group" aria-label="Filter by classification">
          {(['all', 'information', 'incident'] as const).map((value) => (
            <button
              key={value}
              type="button"
              className={`filter-btn ${filter === value ? 'active' : ''}`}
              onClick={() => handleFilterChange(value)}
            >
              {value === 'all' ? 'All' : value.charAt(0).toUpperCase() + value.slice(1)}
            </button>
          ))}
        </div>
      </header>

      {loading && <p className="status">Loading posts…</p>}
      {error && <p className="status error">{error}</p>}

      {!loading && !error && result && result.data.length === 0 && (
        <p className="status">No posts found. Run the Python ingestion service first.</p>
      )}

      {!loading && !error && result && result.data.length > 0 && (
        <>
          <p className="results-count">
            Showing {result.from}–{result.to} of {result.total} posts
          </p>

          <div className="posts-grid">
            {result.data.map((post) => (
              <PostCard
                key={post.id}
                post={post}
                onClick={setSelectedPost}
              />
            ))}
          </div>

          {result.last_page > 1 && (
            <nav className="pagination" aria-label="Pagination">
              <button
                type="button"
                disabled={page <= 1}
                onClick={() => setPage((p) => p - 1)}
              >
                Previous
              </button>
              <span>
                Page {result.current_page} of {result.last_page}
              </span>
              <button
                type="button"
                disabled={page >= result.last_page}
                onClick={() => setPage((p) => p + 1)}
              >
                Next
              </button>
            </nav>
          )}
        </>
      )}

      <PostModal post={selectedPost} onClose={() => setSelectedPost(null)} />
    </div>
  )
}
