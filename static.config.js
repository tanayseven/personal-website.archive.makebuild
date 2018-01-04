import axios from 'axios'
import React from 'react'

const blogList = [
  '2016-03-27-hello-world',
  '2016-07-14-finally-an-android-app',
  '2016-07-18-at-nelkinda-coderetreat',
].sort();

function moduleDataFor(moduleName) {
  return require('./src/posts/'+moduleName).data
}

var posts = [];
blogList.forEach(function(element) {
  posts.push(moduleDataFor(element));
}, this);

export default {
  getSiteProps: () => ({
    title: 'React Static',
  }),
  getRoutes: async () => {
    return [
      {
        path: '/',
      },
      {
        path: '/about',
      },
      {
        path: '/blog',
        getProps: () => ({
          posts,
        }),
        children: posts.map(post => ({
          path: `/post/${post.date.year}/${post.date.month}/${post.date.day}`,
          getProps: () => ({
            post,
          }),
        })),
      },
    ]
  },
}
