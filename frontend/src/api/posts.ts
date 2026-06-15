import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL ?? 'http://127.0.0.1:8000/api'

const client = axios.create({
  baseURL: API_URL,
  headers: {
    Accept: 'application/json',
  },
})

export type Classification = 'information' | 'incident'

export interface Post {
  id: number
  source_url: string
  content: string
  media: string | null
  page_name: string
  post_date: string
  classification: Classification
  created_at: string
  updated_at: string
}

export interface PaginatedPosts {
  current_page: number
  data: Post[]
  first_page_url: string
  from: number | null
  last_page: number
  last_page_url: string
  links: Array<{ url: string | null; label: string; active: boolean }>
  next_page_url: string | null
  path: string
  per_page: number
  prev_page_url: string | null
  to: number | null
  total: number
}

export async function fetchPosts(
  page = 1,
  classification?: Classification | null,
): Promise<PaginatedPosts> {
  const params: Record<string, string | number> = { page, per_page: 12 }

  if (classification) {
    params.classification = classification
  }

  const { data } = await client.get<PaginatedPosts>('/posts', { params })
  return data
}
