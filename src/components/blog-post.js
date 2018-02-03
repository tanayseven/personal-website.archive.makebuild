import React from 'react'
import {MuiThemeProvider} from 'material-ui/styles'
import theme from './theme'
import Card from 'material-ui/Card'
import Typography from 'material-ui/Typography'

class BlogPost extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      children: props.children,
      id: props.data.id,
      tags: props.data.tags,
      date: props.data.date,
      title: props.data.title,
      description: props.data.description,
    }
  }
  render () {
    return (
      <MuiThemeProvider theme={theme}>
        <Typography type='headline' align='center'>
          {this.state.title}
        </Typography>
        <br/>
        <Card
          style={{padding: '20px 20px 20px'}}
        >
          <Typography type='body1'>
            {this.state.children}
          </Typography>
        </Card>
      </MuiThemeProvider>
    )
  }
}

export default BlogPost
