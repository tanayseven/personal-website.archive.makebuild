import React from "react";
import NavBar from "./nav-bar";

export default class Page extends React.Component {
    render() {
        return (
            <div>
                <NavBar />
                <div>{ this.props.content }</div>
            </div>
        );
    }
}
