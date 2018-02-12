import React from 'react'
import Tabs, {Tab} from 'material-ui/Tabs'
import {MuiThemeProvider} from 'material-ui/styles'
import Card from 'material-ui/Card'
import theme from './theme'
import {Link, Redirect, Router} from "react-static";

class NavBar extends React.Component {
  constructor (props) {
    super(props)
    this.pageList = ['', '/', '/resume', '/blog', '/about']
    let selection
    selection = this.pageList.indexOf('/' + props.path.split('/')[1])
    this.state = {
      selection: selection,
      buttonClicked: false,
    }
  }
  handleChange = (event, value) => {
    this.setState({selection: value, buttonClicked: true})
  }
  render () {
    var redirect = null
    if (this.state.buttonClicked) {
      redirect = (
        <Router>
          <Redirect push to={this.pageList[this.state.selection]} />
        </Router>
      )
    }
    return (
        <div
          style={{position: 'fixed', width: '100%', marginTop: '10px'}}
        >
          <nav>
            <div className="nav-wrapper">
              <a href="#" className="brand-logo">Tanay PrabhuDesai</a>
              <ul id="nav-mobile" className="right hide-on-med-and-down">
                <li><Link to="/">Home</Link></li>
                <li><Link to="/resume">Résumé</Link></li>
                <li><Link to="/blog">Blog</Link></li>
                <li><Link to="/about">About Me</Link></li>
              </ul>
            </div>
          </nav>
        </div>
    )
    this.state.buttonClicked = false;
  }
}
export default NavBar
