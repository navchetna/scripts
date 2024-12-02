import { GetServerSideProps } from 'next'
import Layout from '@/components/Layout'
import { BlogPost } from '@/interfaces/BlogPost'
import { Card, CardContent, Typography, Button, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper } from '@mui/material'
import Link from 'next/link'

interface HomeProps {
  posts: BlogPost[]
}

export default function Home({ posts }: HomeProps) {
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
                    <TableCell>{new Date(post.createdAt).toLocaleDateString()}</TableCell>
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
                    {new Date(post.createdAt).toLocaleDateString()} by {post.author}
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

export const getServerSideProps: GetServerSideProps = async () => {
  try {
    // In a real application, you would fetch this data from an API or database
    const posts: BlogPost[] = [
      { id: 1, title: "First Post", content: "This is the first post content.", createdAt: new Date().toISOString(), author: "John Doe" },
      { id: 2, title: "Second Post", content: "This is the second post content.", createdAt: new Date().toISOString(), author: "Jane Smith" },
      { id: 3, title: "Third Post", content: "This is the third post content.", createdAt: new Date(Date.now() - 86400000).toISOString(), author: "Alice Johnson" },
    ]

    return {
      props: {
        posts,
      },
    }
  } catch (error) {
    console.error("Failed to fetch posts:", error)
    return {
      props: {
        posts: [],
      },
    }
  }
}

