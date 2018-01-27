import React from 'react'
import { MuiThemeProvider } from 'material-ui/styles'
import theme from './theme'
import FontAwesome from 'react-fontawesome'
import Card, { CardContent, CardActions } from 'material-ui/Card'
import {IconButton} from "material-ui";
import {Link} from "material-ui-icons";

class SocialSiteCard extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      iconName: props.iconName,
      href: props.href,
    }
  }
  render ()  {
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
            style={{display: 'flex', margin: '0 auto'}}
          >
            <IconButton aria-label={this.state.iconName}>
              <Link />
            </IconButton>
          </CardActions>
        </Card>
      </MuiThemeProvider>
    )
  }
}
export default SocialSiteCard