import React from 'react'
import { getSiteProps } from 'react-static'
//
import logoImg from '../logo.png'

export default getSiteProps(() => (
  <div>
    <div id="social-media-links">
      <a target="_blank" href="https://www.linkedin.com/in/tanay-prabhudesai-1029b073/"><i className="fa fa-linkedin" aria-hidden="true"></i></a>
      <a target="_blank" href="https://plus.google.com/+TanayPrabhuDesai"><i className="fa fa-google" aria-hidden="true"></i></a>
      <a target="_blank" href="https://twitter.com/tanayseven"><i className="fa fa-twitter" aria-hidden="true"></i></a>
      <a target="_blank" href="https://github.com/tanayseven"><i className="fa fa-github" aria-hidden="true"></i></a>
    </div>
    <p>Hi, I'm Tanay PrabhuDesai.</p>
    <p>I'm a software engineer based in Pune, India.</p>
    <p>This website is generated using <a href="https://github.com/tanayseven/personal_website/">Frozen Flask</a></p>
  </div>
))
