import React from "react";
import { MuiThemeProvider, createMuiTheme } from "material-ui/styles";
import purple from "material-ui/colors/purple";
import green from "material-ui/colors/green";

import NavBar from "./nav-bar";

export default class Page extends React.Component {
    render() {
        return (
                <div>
                    <NavBar />
                    <div>{ this.props.children }</div>
                </div>
        );
    }
}

