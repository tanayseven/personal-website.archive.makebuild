const blogList = [
  '2016-03-27-hello-world',
  '2016-07-14-finally-an-android-app',
  '2016-07-18-at-nelkinda-coderetreat',
].sort();

function moduleDataFor(moduleName) {
  const componentPath = './src/posts/'+moduleName;
  let data = require(componentPath).data
  data.componentPath = componentPath
  return data;
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
        component: 'src/containers/Home',
      },
      {
        path: '/about',
        component: 'src/containers/About',
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
    ]
  },
}
