import React, {useEffect, useState} from 'react'
import Layout from '@/components/Layout'
import { BlogPost } from '@/interfaces/BlogPost'
import { Card, CardContent, Typography, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material'
import Link from 'next/link'
import { API_URL } from '@/lib/const'
import axios from 'axios'

interface HomeProps {
  posts: BlogPost[]
}

export default function Home() {
  
  const [posts, setPosts] = useState<BlogPost[]>([])

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const res = await axios.get(`${API_URL}/blogs`)
        setPosts(res.data.data)
      } catch (error) {
        console.error(error)
      }
    }

    fetchPosts()
  }, [])

  return (
    <Layout>
      <div className="space-y-8">
        <div className="flex justify-end">
          <Link href="/create" passHref>
            <Button variant="contained" color="primary">
              Create New Post
            </Button>
          </Link>
        </div>

        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 650 }} aria-label="blog posts table">
            <TableHead>
              <TableRow>
                <TableCell>Date</TableCell>
                <TableCell>Title</TableCell>
                <TableCell>Author</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {posts && posts.length > 0 ? (
                posts.map((post) => (
                  <TableRow key={post.id}>
                    <TableCell>{new Date(post.created_at).toLocaleDateString()}</TableCell>
                    <TableCell>{post.title}</TableCell>
                    <TableCell>{post.author}</TableCell>
                  </TableRow>
                ))
              ) : (
                <TableRow>
                  <TableCell colSpan={3} align="center">No posts available.</TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </TableContainer>

        <Typography variant="h5" component="h2" gutterBottom>
          Recent Posts
        </Typography>
        <div className="space-y-4">
          {posts && posts.length > 0 ? (
            posts.map((post) => (
              <Card key={post.id}>
                <CardContent>
                  <Typography variant="h6" component="h3">
                    {post.title}
                  </Typography>
                  <Typography color="textSecondary" gutterBottom>
                    {new Date(post.created_at).toLocaleDateString()} by {post.author}
                  </Typography>
                  <Typography variant="body2" component="p">
                    {post.content.substring(0, 100)}...
                  </Typography>
                </CardContent>
              </Card>
            ))
          ) : (
            <Typography variant="body1">No posts available.</Typography>
          )}
        </div>
      </div>
    </Layout>
  )
}


