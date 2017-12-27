import React from "react";
import Tabs, { Tab } from "material-ui/Tabs";

export default class NavBar extends React.Component {
    render() {
        return (
            <div>
                <nav>
                    <Tabs>
                        <Tab disabled label="Tanay PrabhuDesai" />
                        <Tab href="/" label="Home" />
                        <Tab href="/blog/" label="Blog" />
                        <Tab href="/resume/" label="Résumé" />
                        <Tab href="/about/" label="About Me" />
                    </Tabs>
                </nav>
            </div>
        )
    }
}
