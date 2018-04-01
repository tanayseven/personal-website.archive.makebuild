import React from 'react'
import { withRouteData, Link } from 'react-static'
import { Post } from '../types'

interface Props {
  posts: Post[]
}

export default withRouteData(({ posts }: Props) => (
  <div>
      {posts.map((post, index) => {
        <div className="row">
          <div className="card">
            <div className="card-image">
              <img src={post.thumb} />
            </div>
            <div className="card-content">
              <span className="card-title">{post.title}</span>
              <span className="text-gray">{post.date}</span>
              {post.description}
            </div>
          </div>
        </div>
      })}

  </div>
))
