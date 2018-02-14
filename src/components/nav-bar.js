import React from 'react'
import {Link} from "react-static";

class NavBarButton extends React.Component {
  constructor(props) {
    super(props)
    const path = typeof window !== 'undefined' ? window.location.pathname : ''
    const buttonClasses = '/' + path.split('/')[1] === this.props.link ? 'active disabled' : ''
    this.state = {
      buttonClasses: buttonClasses
    }
  }
  render() {
    return (
      <li className={this.state.buttonClasses}><Link to={this.props.link}>{this.props.label}</Link></li>
    )
  }
}

class NavBar extends React.Component {
  constructor (props) {
    super(props)
  }
  render () {
    return (
      <nav>
        <div className="nav-wrapper">
          <a className="brand-logo left disabled">Tanay PrabhuDesai</a>
          <ul className="right">
            <NavBarButton link='/' label='Home' />
            <NavBarButton link='/resume' label='Résumé' />
            <NavBarButton link='/blog' label='Blog' />
            <NavBarButton link='/about' label='About Me' />
          </ul>
        </div>
      </nav>
    )
    // this.state.buttonClicked = false;
  }
}
export default NavBar
