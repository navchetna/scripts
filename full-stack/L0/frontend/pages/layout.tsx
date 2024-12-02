import { AppBar, Toolbar, Typography, Container } from '@mui/material'
import { ThemeProvider, createTheme } from '@mui/material/styles'
import CssBaseline from '@mui/material/CssBaseline'

const theme = createTheme()

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <div className="min-h-screen flex flex-col">
            <AppBar position="static">
              <Toolbar>
                <Typography variant="h6" component="div">
                  Full Stack Blog
                </Typography>
              </Toolbar>
            </AppBar>
            <Container className="flex-grow mt-8">
              {children}
            </Container>
          </div>
        </ThemeProvider>
      </body>
    </html>
  )
}

