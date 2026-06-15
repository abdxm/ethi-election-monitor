import type { Post } from '../api/posts'

interface PostModalProps {
  post: Post | null
  onClose: () => void
}

function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleString('en-ET', {
    dateStyle: 'full',
    timeStyle: 'short',
  })
}

export default function PostModal({ post, onClose }: PostModalProps) {
  if (!post) return null

  return (
    <div className="modal-overlay" onClick={onClose} role="presentation">
      <div
        className="modal-content"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
      >
        <button type="button" className="modal-close" onClick={onClose} aria-label="Close">
          ×
        </button>

        <header className="modal-header">
          <h2 id="modal-title">{post.page_name}</h2>
          <span className={`badge badge-${post.classification}`}>
            {post.classification}
          </span>
        </header>

        <time className="modal-date" dateTime={post.post_date}>
          {formatDate(post.post_date)}
        </time>

        {post.media && (
          <img src={post.media} alt="" className="modal-media" />
        )}

        <p className="modal-body">{post.content}</p>

        <footer className="modal-footer">
          <a href={post.source_url} target="_blank" rel="noopener noreferrer">
            View source
          </a>
        </footer>
      </div>
    </div>
  )
}
