import React from 'react'
import Tabs, {Tab} from 'material-ui/Tabs'
import {MuiThemeProvider} from 'material-ui/styles'
import Card from 'material-ui/Card'
import theme from './theme'
import {Link} from "react-static";

class NavBar extends React.Component {
  constructor (props) {
    super(props)
    this.home =
    this.resume = <Link to='/resume'/>
    this.blog = <Link to='/blog'/>
    this.about = <Link to='/about'/>
    this.pageList = ['', '/', '/resume', '/blog', '/about']
    this.state = {
      selection: this.pageList.indexOf('/'+window.location.pathname.split('/')[1]),
    }
  }
  handleChange = (event, value) => {
    this.setState({selection: value})
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
              <Tab to="/" label={<Link to='/'>Home</Link>} onClick={this.home.onClick} />
              <Tab to="/resume" label={<Link to='/resume'>Résumé</Link>} onClick={this.resume.onClick} />
              <Tab to="/blog" label={<Link to='/blog'>Blog</Link>} onClick={this.blog.onClick} />
              <Tab to="/about" label={<Link to='/about'>About</Link>} onClick={this.about.onClick} />
            </Tabs>
          </Card>
        </div>
      </MuiThemeProvider>
    )
  }
}
export default NavBar
