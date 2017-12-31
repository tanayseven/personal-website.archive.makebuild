import React from "react";

import Paper from 'material-ui/Paper';
import Tabs, { Tab } from "material-ui/Tabs";

function TabContainer(props) {
    return (
        <div>{props.children}</div>
    );
}

const navBar = {
  display: 'table',
  margin: 'auto'
}

class NavBar extends React.Component {
    state = {
      value: 0,
    };
  
    handleChange = (event, value) => {
      this.setState({ value });
    };
  
    render() {
      const { classes } = this.props;
      const { value } = this.state;
  
      return (
          <Paper>
            <span>
            <Tabs value={value} onChange={this.handleChange} style={navBar}>
              <Tab disabled label="Tanay PrabhuDesai" />
              <Tab label="Home" href="/" />
              <Tab label="Blog" href="/blog/" />
              <Tab label="Résumé" href="/resume/" />
              <Tab label="About Me" href="/about/" />
            </Tabs>
            </span>
          </Paper>
      );
    }
  }

  export default NavBar;    
