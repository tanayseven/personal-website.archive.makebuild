
import React from 'react'
import { getRouteProps, Switch, Route, Link } from 'react-static'
//
import Post from './Post'

export default getRouteProps(({ match, posts }) => (
  <div>
    <Switch>
      <Route
        path={match.url}
        exact
        render={() => (
          <div>
            <h1>These are all the blogs that I've written.</h1>
            <br />
            All Posts:
            <ul>
              {posts.map(post => (
                <li key={post.id}>
                  <Link to={`/blog/post/${post.date.year}/${post.date.month}/${post.date.day}/`}>{post.title}</Link>
                </li>
              ))}
            </ul>
          </div>
        )}
      />
      <Route path={`${match.url}/post/:postID/`} component={Post} />
    </Switch>
  </div>
))