import WelcomeApp from '../apps/welcome_app/index.vue'
import SearchApp from '../apps/search_app/index.vue'
import NodeApp from '../apps/node_app/index.vue'


export default [
  {
    path: '/',
    component: WelcomeApp
  },
  {
    path: '/search',
    component: SearchApp,
    props: (route) => {
      return route.query;
    }
  },
  {
    path: '/node/ids/:id',
    component: NodeApp,
    props: true
  }
];