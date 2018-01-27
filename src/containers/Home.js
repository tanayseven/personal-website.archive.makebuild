import React from 'react'
import Card, {CardContent} from 'material-ui/Card'
import Grid from 'material-ui/Grid'
import {getSiteProps} from 'react-static'
import 'font-awesome/css/font-awesome.min.css'
import SocialSiteCard from '../components/custom-cards'

export default getSiteProps(() => (
  <div>
    <Grid container spacing={24}>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='linkedin' href='plus.google.com' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='google-plus' href='plus.google.com' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='twitter' href='plus.google.com' />
      </Grid>
      <Grid item xs={6} sm={3}>
        <SocialSiteCard iconName='github' href='plus.google.com' />
      </Grid>
    </Grid>
    <div className='jumbo-text'>
      <p>Hi, I'm Tanay PrabhuDesai.</p>
      <p>I'm a software engineer based in Pune, India.</p>
    </div>
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
