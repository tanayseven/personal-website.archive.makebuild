import React from 'react'
import Tabs, {Tab} from 'material-ui/Tabs'
import {MuiThemeProvider} from 'material-ui/styles'
import Card from 'material-ui/Card'
import theme from './theme'

class NavBar extends React.Component {
  constructor (props) {
    super(props)
    this.pageList = ['', '/', '/resume', '/blog', '/about'],
    this.state = {
      selection: this.pageList.indexOf('/'+window.location.pathname.split('/')[1]),
    }
  }
  handleChange = (event, value) => {
    this.setState({selection: value})
    setTimeout(() => window.open(this.pageList[value], '_self'), 300)
  }
  render () {
    return (
      <MuiThemeProvider theme={theme}>
        <div
          style={{position: 'fixed', width: '100%'}}
        >
          <Card
            raised
            className='top-bar'
            style={{maxWidth: '960px', margin: '0 auto'}}
          >
            <Tabs
              centered
              value={this.state.selection}
              indicatorColor="grey"
              onChange={this.handleChange}
            >
              <Tab label="Tanay PrabhuDesai" disabled />
              <Tab to="/" label="Home" />
              <Tab to="/resume" label="Résumé" />
              <Tab to="/blog" label="Blog" />
              <Tab to="/about" label="About" />
            </Tabs>
          </Card>
        </div>
      </MuiThemeProvider>
    )
  }
}
export default NavBar
