import type { Post } from '../api/posts'

interface PostCardProps {
  post: Post
  onClick: (post: Post) => void
}

function formatDate(dateString: string): string {
  return new Date(dateString).toLocaleString('en-ET', {
    dateStyle: 'medium',
    timeStyle: 'short',
  })
}

export default function PostCard({ post, onClick }: PostCardProps) {
  const preview =
    post.content.length > 180 ? `${post.content.slice(0, 180)}…` : post.content

  return (
    <article className="post-card" onClick={() => onClick(post)} role="button" tabIndex={0}
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault()
          onClick(post)
        }
      }}>
      <div className="post-card-header">
        <span className="page-name">{post.page_name}</span>
        <span className={`badge badge-${post.classification}`}>
          {post.classification}
        </span>
      </div>

      {post.media && (
        <img
          src={post.media}
          alt=""
          className="post-card-media"
          loading="lazy"
        />
      )}

      <p className="post-card-content">{preview}</p>
      <time className="post-card-date" dateTime={post.post_date}>
        {formatDate(post.post_date)}
      </time>
    </article>
  )
}
