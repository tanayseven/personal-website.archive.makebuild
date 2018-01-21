import React from 'react'
import Paper from 'material-ui/Paper'
import Tabs, { Tab } from 'material-ui/Tabs'
import { MuiThemeProvider } from 'material-ui/styles'
import theme from './theme'

class NavBar extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      selection: 1,
    }
  }
  handleChange = (event, value) => {
    this.setState({selection: value})
  }
  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <Paper>
          <Tabs
            centered
            value={this.state.selection}
            indicatorColor="primary"
            textColor="primary"
            onChange={this.handleChange}
          >
            <Tab label="Tanay PrabhuDesai" disabled />
            <Tab to="/" label="Home" />
            <Tab to="/resume" label="Résumé" />
            <Tab to="/blog" label="Blog" />
            <Tab to="/about" label="About" />
          </Tabs>
        </Paper>
      </MuiThemeProvider>
    )
  }
}
export default NavBar