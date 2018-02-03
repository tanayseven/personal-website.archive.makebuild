import React from 'react'
import {Router} from 'react-static'
import Routes from 'react-static-routes'

import 'typeface-roboto'

import NavBar from './components/nav-bar'

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
      <div style={{maxWidth: '760px', padding: '70px 1rem 1rem', margin: '0 auto'}} >
        <Routes />
      </div>
    </div>
  </Router>
)
