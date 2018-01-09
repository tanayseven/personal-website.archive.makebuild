const blogList = [
  '2016-03-27-hello-world',
  '2016-07-14-finally-an-android-app',
  '2016-07-18-at-nelkinda-coderetreat',
].sort()

function moduleDataFor (moduleName) {
  const componentPath = `./src/posts/${moduleName}`
  /* eslint-disable */
  const data = require(componentPath).data
  /* eslint-enable */
  data.componentPath = componentPath
  return data
}

const posts = []
blogList.forEach(element => {
  posts.push(moduleDataFor(element))
}, this)
export default {
  getSiteProps: () => ({
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
      getProps: () => ({
        posts,
      }),
      children: posts.map(post => ({
        path: `/post/${post.id}`,
        component: post.componentPath,
        getProps: () => ({
          post,
        }),
      })),
    },
    {
      is404: true,
      component: 'src/containers/404',
    },
  ],
}
