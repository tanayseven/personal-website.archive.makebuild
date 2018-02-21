import React from 'react'
import Tabs, {Tab} from 'material-ui/Tabs'
import { mount, shallow } from 'enzyme'
import NavBar from '../../src/components/nav-bar'
import {Redirect} from "react-static";

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

  it('should activate "home" tab when the path is set as "/"', () => {
    const tabs = shallow(<NavBar path='/' />).find(Tabs)
    expect(tabs.props().value).toBe(1)
  })


  it('should activate "resume" tab when the path is set as "/resume"', () => {
    const tabs = shallow(<NavBar path='/resume' />).find(Tabs)
    expect(tabs.props().value).toBe(2)
  })

  it('should activate "blog" tab when the path is set as "/blog"', () => {
    const tabs = shallow(<NavBar path='/blog' />).find(Tabs)
    expect(tabs.props().value).toBe(3)
  })

  it('should activate "about" tab when the path is set as "/about"', () => {
    const tabs = shallow(<NavBar path='/about' />).find(Tabs)
    expect(tabs.props().value).toBe(4)
  })

  it('should render redirect when any one of the tabs is clicked on', () => {
    const wrapper = mount(<NavBar path='/' />)
    wrapper.find(Tab).at(1).simulate('click')
    wrapper.update()
    expect(wrapper.find(Redirect).length).toBeGreaterThan(0)
  })

  it('should not render redirect when any one of the tabs is not clicked', () => {
    const wrapper = shallow(<NavBar path='/' />)
    expect(wrapper.find(Redirect).length).toBe(0)
  })

})
