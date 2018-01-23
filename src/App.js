import React from 'react'
import { Router, Link } from 'react-static'
import Routes from 'react-static-routes'

import 'typeface-roboto'
import Paper from 'material-ui/Paper'
import Tabs, { Tab } from 'material-ui/Tabs'

import NavBar from './components/nav-bar'

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
      <NavBar />
      <div className="content">
        <Routes />
      </div>
    </div>
  </Router>
)
