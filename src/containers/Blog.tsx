import React from 'react'
import { withRouteData, Link } from 'react-static'
import { Post } from '../types'

interface Props {
  posts: Post[]
}

export default withRouteData(({ posts }: Props) => {
  return (<div>
      <span>My blog, this is a place I call my public diary</span>
      {posts.map((post, index) => 
        <div className="row">
          <div className="card">
            <div className="card-image">
              {/* <img src={post.thumb} /> */}
            </div>
            <div className="card-content">
              <span className="card-title">{post.title}</span>
              {/* <span className="text-gray">{post.date}</span> */}
              {/* {post.body} */}
            </div>
            <div className="card-action">
              <Link to={'/blog/post/' + post.current_page_name} >Read</Link>
            </div>
          </div>
        </div>
      )}
  </div>)
})
