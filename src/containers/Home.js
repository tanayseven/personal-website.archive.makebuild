import React from 'react'
import Card from 'material-ui/Card'
import Grid from 'material-ui/Grid'
import {getSiteProps} from 'react-static'

export default getSiteProps(() => (
  <div>
    <div id="social-media-links">
      <a target="_blank" href="https://www.linkedin.com/in/tanay-prabhudesai-1029b073/">Linkedin</a>
      <a target="_blank" href="https://plus.google.com/+TanayPrabhuDesai">Google +</a>
      <a target="_blank" href="https://twitter.com/tanayseven">Twitter</a>
      <a target="_blank" href="https://github.com/tanayseven">Github</a>
    </div>
    <p>Hi, I'm Tanay PrabhuDesai.</p>
    <p>I'm a software engineer based in Pune, India.</p>
    <div>
      <Grid container>
        <Card className='project-card'>
          <CardContent>
        Something
          </CardContent>
        </Card>
        <Card className='project-card'>
          <CardContent>
        Something
          </CardContent>
        </Card>
      </Grid>
    </div>
  </div>
))
