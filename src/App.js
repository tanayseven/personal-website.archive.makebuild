import React from 'react'
import { Router, Link } from 'react-static'
import Routes from 'react-static-routes'

import './app.css'

const styles = theme => ({
  root: {
    flexGrow: 1,
    marginTop: theme.spacing.unit * 3,
    backgroundColor: theme.palette.background.paper,
  },
})

const navBarStyle = {
  display: 'inline-block',
  'list-style-type': 'none',
}

export default () => (
  <Router>
    <div>
      <nav>
        <span style={navBarStyle}>Tanay PrabhuDesai</span>
        <Link to="/" style={navBarStyle}>Home</Link>
        <Link to="/resume" style={navBarStyle}>Résumé</Link>
        <Link to="/blog" style={navBarStyle}>Blog</Link>
        <Link to="/about" style={navBarStyle}>About</Link>
      </nav>
      <div className="content">
        <Routes />
      </div>
    </div>
  </Router>
)
