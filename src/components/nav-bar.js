import React from "react";

export default class NavBar extends React.Component {
    render() {
        return (
            <div>
                <h1>Tanay PrabhuDesai</h1>
                <nav>
                    <a href="/">Home</a>
                    <a href="/blog/">Blog</a>
                    <a href="/resume/">Résumé</a>
                    <a href="/about/">About Me</a>
                </nav>
            </div>
        )
    }
}
