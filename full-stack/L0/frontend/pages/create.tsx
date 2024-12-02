import { useState } from 'react'
import { useRouter } from 'next/router'
import Layout from '@/components/Layout'
import { TextField, Button, Typography } from '@mui/material'

export default function CreatePost() {
  const [title, setTitle] = useState('')
  const [content, setContent] = useState('')
  const [author, setAuthor] = useState('')
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    // In a real application, you would send this data to an API
    console.log({ title, content, author })
    // Redirect to home page after creation
    router.push('/')
  }

  return (
    <Layout>
      <Typography variant="h4" component="h1" gutterBottom>
        Create New Post
      </Typography>
      <form onSubmit={handleSubmit} className="space-y-4">
        <TextField
          label="Title"
          variant="outlined"
          fullWidth
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <TextField
          label="Author"
          variant="outlined"
          fullWidth
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          required
        />
        <TextField
          label="Content"
          variant="outlined"
          fullWidth
          multiline
          rows={4}
          value={content}
          onChange={(e) => setContent(e.target.value)}
          required
        />
        <Button type="submit" variant="contained" color="primary">
          Create Post
        </Button>
      </form>
    </Layout>
  )
}

