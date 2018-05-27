import WelcomeApp from '../apps/welcome_app/index.vue'
import SearchApp from '../apps/search_app/index.vue'


export default [
  {
    path: '/',
    component: WelcomeApp
  },
  {
    path: '/search',
    component: SearchApp
  }
];