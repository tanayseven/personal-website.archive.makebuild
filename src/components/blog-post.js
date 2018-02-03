import React from 'react'
import {MuiThemeProvider} from 'material-ui/styles'
import theme from './theme'
import Card from 'material-ui/Card'
import Typography from 'material-ui/Typography'
import {Redirect} from "react-static";
import FontAwesome from 'react-fontawesome'
import Button from "material-ui/Button";

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
      goBack: false,
    }
  }
  goBack = () => {
    this.setState({goBack: true})
  }
  render () {
    var redirect = null;
    if (this.state.goBack) {
      redirect = <Redirect push to='/blog/' />
    }
    this.state.goBack = false
    return (
      <MuiThemeProvider theme={theme}>
        {redirect}
        <Button
          fab mini
          onClick={this.goBack}
          style={{position: 'fixed'}}
        >
          <FontAwesome
            name='angle-left'
          />
        </Button>
        <Typography type='headline' align='center'>
          {this.state.title}
        </Typography>
        <br/>
        <Card
          style={{padding: '20px 20px 20px'}}
        >
          <Typography type='body2'>
            {this.state.children}
          </Typography>
        </Card>
      </MuiThemeProvider>
    )
  }
}

export default BlogPost
