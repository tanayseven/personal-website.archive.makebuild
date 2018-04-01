import path from 'path'
import React from 'react'

// import { blogList } from './active-blog-list'

// Paths Aliases defined through tsconfig.json
const typescriptWebpackPaths = require('./webpack.config.js')

import posts from './src/posts/index'

// function moduleDataFor (moduleName) {
//   const componentPath = `./src/posts/${moduleName}`
//   /* eslint-disable */
//   const data = require(componentPath).data
//   /* eslint-enable */
//   data.componentPath = componentPath
//   return data
// }

// const posts = []
// blogList.forEach(element => {
//   posts.push(moduleDataFor(element))
// }, this)


export default {
  entry: path.join(__dirname, 'src', 'index.tsx'),
  getSiteData: () => ({
    title: 'React Static',
  }),
  getRoutes: async () => [
    {
      path: '/',
      component: 'src/containers/Home',
    },
    {
      path: '/about',
      component: 'src/containers/About',
    },
    {
      path: '/resume',
      component: 'src/containers/Resume',
    },
    {
      path: '/blog',
      component: 'src/containers/Blog',
      getData: () => ({
        posts,
      }),
      children: posts.map(post => ({
        path: `/post/${post.id}`,
        component: post.componentPath,
        getData: () => ({
          post,
        }),
      })),
    },
    {
      is404: true,
      component: 'src/containers/404',
    },
  ],
  webpack: (config, { defaultLoaders }) => {
    // Add .ts and .tsx extension to resolver
    config.resolve.extensions.push('.ts', '.tsx')

    // Add TypeScript Path Mappings (from tsconfig via webpack.config.js)
    // to react-statics alias resolution
    config.resolve.alias = typescriptWebpackPaths.resolve.alias

    // We replace the existing JS rule with one, that allows us to use
    // both TypeScript and JavaScript interchangeably
    config.module.rules = [
      {
        oneOf: [
          {
            test: /\.(js|jsx|ts|tsx)$/,
            exclude: defaultLoaders.jsLoader.exclude, // as std jsLoader exclude
            use: [
              {
                loader: 'babel-loader',
              },
              {
                loader: require.resolve('ts-loader'),
                options: {
                  transpileOnly: true,
                },
              },
            ],
          },
          defaultLoaders.cssLoader,
          defaultLoaders.fileLoader,
        ],
      },
    ]
    return config
  },
  Document: ({
    Html, Head, Body, children,
  }) => (
    <Html lang="en-US">
      <Head>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css" />
        <title>Tanay PrabhuDesai</title>
      </Head>
      <Body>
        {children}
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js" />
      </Body>
    </Html>
  ),
}
