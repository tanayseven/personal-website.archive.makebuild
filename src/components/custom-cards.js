import React from 'react'
import {MuiThemeProvider} from 'material-ui/styles'
import theme from './theme'
import FontAwesome from 'react-fontawesome'
import Card, {CardActions, CardContent} from 'material-ui/Card'
import Typography from 'material-ui/Typography'
import Button from 'material-ui/Button'
import {Redirect} from "react-static";

class SocialSiteCard extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      iconName: props.iconName,
      href: props.href,
    }
  }
  openLinkOnNewPage () {
    setTimeout(() => window.open(this.state.href, '_blank'), 300)
  }
  render () {
    return (
      <MuiThemeProvider theme={theme}>
        <Card
          style={{display: 'flex', height: '140px', flexDirection: 'column'}}
        >
          <CardContent
            style={{display: 'flex', margin: '0 auto'}}
          >
            <FontAwesome
              name={this.state.iconName}
              size='4x'
            />
          </CardContent>
          <CardActions
            style={{display: 'flex', margin: '0', paddingBottom: '10px'}}
          >
            <Button
              aria-label={this.state.iconName}
              fab mini
              onClick={this.openLinkOnNewPage.bind(this)}
            >
              <FontAwesome
                name='external-link'
              />
            </Button>
          </CardActions>
        </Card>
      </MuiThemeProvider>
    )
  }
}

class PersonalProjectCard extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      title: props.title,
      description: props.description,
      liveLink: props.liveLink,
      githubLink: props.githubLink,
    }
  }
  openLiveLinkOnNewPage () {
    setTimeout(() => window.open(this.state.liveLink, '_blank'), 300)
  }
  openGithubLinkOnNewPage () {
    setTimeout(() => window.open(this.state.githubLink, '_blank'), 300)
  }
  render () {
    const liveLinkButton = this.state.liveLink ?
      <Button
        aria-label={this.state.iconName}
        fab mini
        onClick={this.openLiveLinkOnNewPage.bind(this)}
      >
        <FontAwesome
          name='external-link'
        />
      </Button>
      :
      ''
    const githubButton = this.state.githubLink ?
      <Button
        aria-label={this.state.iconName}
        fab mini
        onClick={this.openGithubLinkOnNewPage.bind(this)}
      >
        <FontAwesome
          name='github'
        />
      </Button>
      :
      ''
    return (
      <MuiThemeProvider theme={theme}>
        <Card
          style={{display: 'flex', height: '160px', flexDirection: 'column', paddingBottom: '10px'}}
        >
          <CardContent
            style={{display: 'flex', flexDirection: 'column'}}
          >
            <Typography type='title'>
              {this.state.title}
            </Typography>
            <Typography component='p'>
              {this.state.description}
            </Typography>
          </CardContent>
          <CardActions
            style={{display: 'flex', margin: '0 auto'}}
          >
            {liveLinkButton}
            {githubButton}
          </CardActions>
        </Card>
      </MuiThemeProvider>
    )
  }
}

class BlogCard extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      title: props.title,
      description: props.description,
      date: props.date,
      href: props.href,
      blogToBeOpened: false,
    }
  }
  openBlogOnCurrentPage = function () {
    this.setState({blogToBeOpened: true})
    console.log('outputted')
  }
  render () {
    var redirect = null
    if (this.state.blogToBeOpened) {
      redirect = <Redirect push to={this.state.href} />
    }
    this.state.blogToBeOpened = false
    return (
      <MuiThemeProvider theme={theme}>
        {redirect}
        <Card
          style={{display: 'flex', minHeight: '80px', flexDirection: 'row', paddingBottom: '10px'}}
        >
          <CardContent
            style={{display: 'flex', flexDirection: 'column'}}
          >
            <Typography type='caption'>
              {this.state.date}
            </Typography>
            <Typography type='title'>
              {this.state.title}
            </Typography>
            <Typography>
              {this.state.description}
            </Typography>
          </CardContent>
          <CardActions
            style={{display: 'flex', margin: '0 auto'}}
          >
            <Button
              aria-label={this.state.iconName}
              fab mini
              onClick={this.openBlogOnCurrentPage.bind(this)}
            >
              <FontAwesome
                name='chevron-right'
              />
            </Button>
          </CardActions>
        </Card>
      </MuiThemeProvider>
    )
  }
}

export { PersonalProjectCard, SocialSiteCard, BlogCard }
