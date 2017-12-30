import React from "react";

import { MuiThemeProvider, createMuiTheme, withStyles } from "material-ui/styles";
import purple from 'material-ui/colors/purple';
import green from 'material-ui/colors/green';
import red from 'material-ui/colors/red';

import NavBar from "./nav-bar";

const theme = createMuiTheme({
  palette: {
    primary: purple, // TODO Temporary theme, needs to be changed
    secondary: {
      ...green,
      A400: '#00e677',
    },
    error: red,
  },
});

const styles = {
    div: {
        width: '80%',
        margin: '0 auto',
    }
};

class Page extends React.Component {
    render() {
        return (
            <MuiThemeProvider theme={theme}>
                <div>
                    <NavBar />
                    <div>{ this.props.children }</div>
                </div>
            </MuiThemeProvider>
        );
    }
}

export default withStyles(styles)(Page);

