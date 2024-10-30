import './bootstrap'
import { createApp }                        from 'vue'

import master                               from './components/master.vue'
//import { createRouter, createWebHistory }   from 'vue-router'

import 'vuetify/styles'
import { createVuetify }                    from 'vuetify'
import * as components                      from 'vuetify/components'
import * as directives                      from 'vuetify/directives'
import { es }                               from 'vuetify/locale'
import '@mdi/font/css/materialdesignicons.css'


/*import master                               from './components/master.vue'

import users                                from './components/users.vue'
import contests                             from './components/contests.vue'
import toplist                              from './components/toplist.vue'
import store                                from './store'
*/

const vuetify = createVuetify({
  components,
  directives,
  locale: {
    locale: 'es',
    fallback: 'es',
    messages: { es},
  }
})

/*const router  = createRouter({
  history: createWebHistory(),
  routes: [
      { path: '/',                      component: users },
      { path: '/users',                 component: users },
      { path: '/users/:id_user',        component: users },
      { path: '/contests',              component: contests },
      { path: '/contests/:id_contest',  component: contests},
      { path: '/toplist',               component: toplist },
      { path: '/toplist/:id_project',   component: toplist }
  ],
})*/

createApp(master)
  //.use(store)
  .use(vuetify)
  //.use(router)
  .mount('#index')

