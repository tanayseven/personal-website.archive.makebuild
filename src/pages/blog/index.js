import React from "react";
import NavBar from "../../components/nav-bar";
import Page from "../../components/page";
const blogList = [
    '2016-03-27-hello-world',
    '2016-07-14-finally-an-android-app',
    '2016-07-18-at-nelkinda-coderetreat',
].sort();

var blog = [];
function moduleDataFor(moduleName) {
    return require('./'+moduleName).data
}

blogList.forEach(function(element) {
    blog.push(<a href={ element }><p>{ moduleDataFor(element).title }</p></a>);
}, this);

export default () => {
    return (
        <Page
            content={
                <div>
                    <p>{ blog }</p>
                </div>
            } />
    )   
}