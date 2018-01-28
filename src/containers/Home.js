import React from 'react'
import Grid from 'material-ui/Grid'
import {getSiteProps} from 'react-static'
import 'font-awesome/css/font-awesome.min.css'
import {PersonalProjectCard, SocialSiteCard} from '../components/custom-cards'
import Typography from 'material-ui/Typography'

export default getSiteProps(() => (
  <div>
    <Typography type='display1'>
      <p>Hi, I'm Tanay PrabhuDesai.</p>
      <p>I'm a software engineer based in Pune, India.</p>
    </Typography>
    <Typography type='headline'>
      <p>You can connect with me here</p>
    </Typography>
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
    <Typography type='headline'>
      <p>These are some of my personal projects</p>
    </Typography>
    <Grid container spacing={24}>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard
          title='Project Name'
          description='This is some description. That description is needed to tell something about the project in brief'
          liveLink='https://tanayseven.com'
          githubLink='https://github.com/tanayseven'
        />
      </Grid>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard title='Project Name' description='This is some description. That description is needed to tell something about the project in brief' />
      </Grid>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard title='Project Name' description='This is some description. That description is needed to tell something about the project in brief' />
      </Grid>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard title='Project Name' description='This is some description. That description is needed to tell something about the project in brief' />
      </Grid>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard title='Project Name' description='This is some description. That description is needed to tell something about the project in brief' />
      </Grid>
      <Grid item xs={12} sm={6}>
        <PersonalProjectCard title='Project Name' description='This is some description. That description is needed to tell something about the project in brief' />
      </Grid>
    </Grid>
  </div>
))
