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

export default () => (
  <Router>
    <div>
      <nav>
        <span >Tanay PrabhuDesai</span>
        <Link to="/">Home</Link>
        <Link to="/resume">Résumé</Link>
        <Link to="/blog">Blog</Link>
        <Link to="/about">About</Link>
      </nav>
      <div className="content">
        <Routes />
      </div>
    </div>
  </Router>
)
