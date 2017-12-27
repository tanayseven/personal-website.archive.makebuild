import React from "react";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";

import NavBar from "./nav-bar";

export default class Page extends React.Component {
    render() {
        return (
            <MuiThemeProvider>
            <div>
                <NavBar />
                <div>{ this.props.children }</div>
            </div>
            </MuiThemeProvider>
        );
    }
}
