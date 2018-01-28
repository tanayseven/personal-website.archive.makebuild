import React from 'react'
import Card, {CardContent} from 'material-ui/Card'
import Grid from 'material-ui/Grid'
import {getSiteProps} from 'react-static'
import 'font-awesome/css/font-awesome.min.css'
import SocialSiteCard from '../components/custom-cards'
import Typography from 'material-ui/Typography'

export default getSiteProps(() => (
  <div>
    <Grid container spacing={24}>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='linkedin' href='https://www.linkedin.com/in/tanay-prabhudesai-1029b073/' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='google-plus' href='https://plus.google.com/+TanayPrabhuDesai' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='twitter' href='https://twitter.com/tanayseven' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='github' href='https://github.com/tanayseven/' />
      </Grid>
    </Grid>
    <Typography type='display1'>
      <p>Hi, I'm Tanay PrabhuDesai.</p>
      <p>I'm a software engineer based in Pune, India.</p>
    </Typography>
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
