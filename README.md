# Personal Website - Tanay PrabhuDesai

![build-status](https://travis-ci.org/tanayseven/personal_website.svg?branch=master)
[![Website](https://img.shields.io/website-up-down-green-red/https/tanayseven.com.svg?label=hosted_on_server)](https://tanayseven.com)
[![License](https://img.shields.io/github/license/tanayseven/personal_website.svg)](LICENSE.txt)
[![Code Climate](https://img.shields.io/codeclimate/coverage/github/tanayseven/personal_website.svg)](https://codeclimate.com/github/tanayseven/personal_website)

This example includes:

- CSS imports
- Image imports
- File imports
- Custom routing

To get started, run `react-static create` and use the `custom-routing` template.

## Automatic component routing vs custom routing

In automatic component routing, you setup your routes in getRoutes of static.config.js, where you specify the path and the appropriate component for that path:  
`{path: 'foo', component: 'src/components/MyFoo'}` This is the easiest way to specify routes.

In custom component routing, you also setup your routes in getRoutes of the static.config.js, but you don't specify the component! `{path: 'foo'}` Instead, you specify the routes in the components `<Route path='/foo' component={MyFoo} \>`. It's important to note that you can use one method or the other, but not both.

**Note:** automatic routes will be generated even if a given route is not allowed in your custom routing logic. The consequences of a mismatch between _custom_ and _automatic_ routing can be important: you can create the illusion that a route is `not found` on the client (`react-router` not matching a given URL), while a corresponding `index.html` and `routeData.json` were made **available** on the server at build-time. Appending `/routeData.json` to any given URL can help you realize if there is a unwanted mismatch: if `/posts/27/` returns `404` while browsing, so should `/posts/27/routeData.json`.
