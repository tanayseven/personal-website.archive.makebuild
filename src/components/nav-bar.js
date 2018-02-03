import React from 'react'
import Tabs, {Tab} from 'material-ui/Tabs'
import {MuiThemeProvider} from 'material-ui/styles'
import Card from 'material-ui/Card'
import theme from './theme'
import {Redirect} from "react-static";

class NavBar extends React.Component {
  constructor (props) {
    super(props)
    this.pageList = ['', '/', '/resume', '/blog', '/about']
    this.state = {
      selection: this.pageList.indexOf('/'+window.location.pathname.split('/')[1]),
      buttonClicked: false,
    }
  }
  handleChange = (event, value) => {
    this.setState({selection: value, buttonClicked: true})
  }
  render () {
    var redirect = null
    if (this.state.buttonClicked) {
      redirect = <Redirect push to={this.pageList[this.state.selection]} />
    }
    this.state.buttonClicked = false;
    return (
      <MuiThemeProvider theme={theme}>
        {redirect}
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
              <Tab to="/" label='Home' onClick={()=>this.state.selection='/'} />
              <Tab to="/resume" label='Résumé' onClick={()=>this.state.selection='/resume'} />
              <Tab to="/blog" label='Blog' onClick={()=>this.state.selection='/blog'} />
              <Tab to="/about" label='About' onClick={()=>this.state.selection='/about'} />
            </Tabs>
          </Card>
        </div>
      </MuiThemeProvider>
    )
  }
}
export default NavBar
