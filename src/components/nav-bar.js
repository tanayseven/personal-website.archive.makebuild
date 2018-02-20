import React from 'react'
import {Link} from "react-static";

class NavBar extends React.Component {
  constructor (props) {
    super(props)
  }

  compareCurrentLocationWith(link) {
    return link === '/' + window.location.pathname.split('/')[1] ? 'active disabled' : ''
  }

  render () {
    return (
      <nav>
        <div className="nav-wrapper">
          <a className="brand-logo left disabled">Tanay PrabhuDesai</a>
          <ul className="right">
            <li className={this.compareCurrentLocationWith('/')}>
              <Link to='/'>Home</Link>
            </li>
            <li className={this.compareCurrentLocationWith('/resume')}>
              <Link to='/resume'>Résumé</Link>
            </li>
            <li className={this.compareCurrentLocationWith('/blog')}>
              <Link to='/blog'>Blog</Link>
            </li>
            <li className={this.compareCurrentLocationWith('/about')}>
              <Link to='/about'>About Me</Link>
            </li>
          </ul>
        </div>
      </nav>
    )
  }
}
export default NavBar
