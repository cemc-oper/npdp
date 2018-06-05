import WelcomeApp from '../apps/welcome_app/index.vue'
import SearchApp from '../apps/search_app/index.vue'
import NodeApp from '../apps/node_app/index.vue'
import NodeLabelApp from '../apps/node_app/node_label_app.vue'
import NodeInfoApp from '../apps/node_app/node_info_app.vue'


export default [
  {
    name: 'welcome',
    path: '/',
    component: WelcomeApp,
  },
  {
    name: 'search',
    path: '/search',
    component: SearchApp,
    props: (route) => {
      return route.query;
    },
  },
  {
    path: '/node/ids/:id',
    component: NodeApp,
    props: true,
    children: [
      {
        name: 'node_by_id',
        path: '',
        component: NodeInfoApp
      },
      {
        name: 'node_by_id_and_label',
        path: 'labels/:label',
        component: NodeLabelApp,
        props: true,
      }
    ]
  },
];