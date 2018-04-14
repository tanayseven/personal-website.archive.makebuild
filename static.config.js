import path from 'path'
import React from 'react'
import fs from 'fs'

const typescriptWebpackPaths = require('./webpack.config.js')

const blogList = [
  '2016-03-27-hello-world.fjson',
  '2016-07-14-finally-an-android-app.fjson',
  '2016-07-18-at-nelkinda-coderetreat.fjson',
  '2018-01-03-sicp-challenge.fjson',
].sort().reverse()

export default {
  entry: path.join(__dirname, 'src', 'index.tsx'),
  getSiteData: () => ({
    title: 'React Static',
  }),
  getRoutes: async () => {
    const posts = blogList.map(filename => {
      return JSON.parse(fs.readFileSync('./posts/' + filename, 'utf-8'))
    })
    return [
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
          path: `/post/${post.current_page_name}`,
          component: 'src/containers/Post',
          getData: () => ({
            post,
          }),
        })),
      },
      {
        is404: true,
        component: 'src/containers/404',
      },
    ]
  },
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
        <link rel="stylesheet" href="/main.css" />
        <title>Tanay PrabhuDesai</title>
      </Head>
      <Body>
        {children}
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js" />
      </Body>
    </Html>
  ),
}
