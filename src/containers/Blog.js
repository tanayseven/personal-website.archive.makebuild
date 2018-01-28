import React from 'react'
import {getRouteProps} from 'react-static'
import Typography from 'material-ui/Typography'
import {BlogCard} from '../components/custom-cards'

export default getRouteProps(({ posts }) => (
  <div>
    <Typography type='title'>
      <p>These are all my blog posts, I also call it my public diary</p>
    </Typography>
    <br />
    {posts.map((post, index) => (
      <div>
        <BlogCard
          key={post.id + index}
          title={post.title}
          description={post.description}
          date={post.date.year + '-' + post.date.month + '-' + post.date.day}
          href={`/blog/post/${post.id}/`}
        />
        <br />
      </div>
    ))}
  </div>
))
