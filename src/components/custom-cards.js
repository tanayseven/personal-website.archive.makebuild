import React from 'react'
import {MuiThemeProvider} from 'material-ui/styles'
import theme from './theme'
import FontAwesome from 'react-fontawesome'
import Card, {CardActions, CardContent} from 'material-ui/Card'
import Typography from 'material-ui/Typography'
import Button from 'material-ui/Button'

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
            style={{display: 'flex', margin: '0', 'padding-bottom': '10px'}}
          >
            <Button
              aria-label={this.state.iconName}
              fab mini
              onClick={this.openLinkOnNewPage.bind(this)}
            >
              <FontAwesome
                name='link'
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
    this.state = {}
  }
  render () {
    return (
      <MuiThemeProvider theme={theme}>
        <Card
          style={{display: 'flex', height: '140px', flexDirection: 'column'}}
        >
          <CardContent
            style={{display: 'flex', flexDirection: 'column'}}
          >
            <Typography type='title'>
              Project Name
            </Typography>
            <Typography component='p'>
              {'Some short description about the project that was made. What all things were there in that project. How it was written.'}
            </Typography>
          </CardContent>
          <CardActions
            style={{display: 'flex', margin: '0 auto'}}
          >
          </CardActions>
        </Card>
      </MuiThemeProvider>
    )
  }
}

export { PersonalProjectCard, SocialSiteCard }
