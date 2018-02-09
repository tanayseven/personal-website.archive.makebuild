import React from 'react'
import { mount } from 'enzyme'
import NavBar from '../../src/components/nav-bar'

describe('NavBar', () => {
  let props
  let mountedNavBar
  const navBar = () => {
    if (!mountedNavBar) {
      mountedNavBar = mount(
        <NavBar {...props}/>
      )
    }
    return mountedNavBar
  }

  beforeEach(() => {
    props = {
      path: '/'
    }
    mountedNavBar = undefined
  })

  it ('always renders a div', () => {
    const divs = navBar().find('div')
    expect(divs.length).toBeGreaterThan(0)
  })

})
