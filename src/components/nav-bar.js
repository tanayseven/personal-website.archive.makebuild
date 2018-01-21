import React from 'react'
import Paper from 'material-ui/Paper'
import Tabs, { Tab } from 'material-ui/Tabs'


class NavBar extends React.Component {
  render() {
    return (
      <Paper>
        <Tabs
          centered
        >
          <Tab label="Tanay PrabhuDesai" disabled />
          <Tab to="/" label="Home" />
          <Tab to="/resume" label="Résumé" />
          <Tab to="/blog" label="Blog" />
          <Tab to="/about" label="About" />
        </Tabs>
      </Paper>
    )
  }
}
export default NavBar;