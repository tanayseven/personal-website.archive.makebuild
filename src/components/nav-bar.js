import React from "react";
import Tabs, { Tab } from "material-ui/Tabs";
import PropTypes from 'prop-types';
import { withStyles } from 'material-ui/styles';
import AppBar from 'material-ui/AppBar';
import Typography from 'material-ui/Typography';

function TabContainer(props) {
    return (
        <Typography component="div" style={{ padding: 8 * 3 }}>
        {props.children}
        </Typography>
    );
}

TabContainer.propTypes = {
    children: PropTypes.node.isRequired,
};

const styles = theme => ({
    root: {
        flexGrow: 1,
        marginTop: theme.spacing.unit * 3,
        backgroundColor: theme.palette.background.paper,
    },
});

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
        <div className={classes.root}>
          <AppBar position="static">
            <Tabs value={value} onChange={this.handleChange}>
              <Tab disabled label="Tanay PrabhuDesai" />
              <Tab label="Home" href="/" />
              <Tab label="Blog" href="/blog/" />
              <Tab label="Résumé" href="/resume/" />
              <Tab label="About Me" href="/about/" />
            </Tabs>
          </AppBar>
          {value === 0 && <TabContainer>Item One</TabContainer>}
          {value === 1 && <TabContainer>Item Two</TabContainer>}
          {value === 2 && <TabContainer>Item Three</TabContainer>}
        </div>
      );
    }
  }
NavBar.propTypes = {
    classes: PropTypes.object.isRequired,
  };

  export default withStyles(styles)(NavBar);

// class NavBar extends React.Component {
//     render() {
//         return (
//             <div>
//                 <nav>
//                     <Tabs>
//                         <Tab disabled label="Tanay PrabhuDesai" />
//                         <Tab href="/" label="Home" />
//                         <Tab href="/blog/" label="Blog" />
//                         <Tab href="/resume/" label="Résumé" />
//                         <Tab href="/about/" label="About Me" />
//                     </Tabs>
//                 </nav>
//             </div>
//         )
//     }
// }
