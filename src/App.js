import React from 'react'
import {Router} from 'react-static'
import Routes from 'react-static-routes'

import 'typeface-roboto'

import './app.css'
import './css/materialize.min.css'

import NavBar from './components/nav-bar'

const windowVar = typeof window === undefined ? window : ''

export default () => (
  <Router>
    <div style={{backgroundColor: '#eeeeee', margin: 0}}>
      <NavBar path={windowVar} />
      <div style={{maxWidth: '760px', padding: '70px 1rem 1rem', margin: '0 auto'}} >
        <Routes />
      </div>
    </div>
  </Router>
)
