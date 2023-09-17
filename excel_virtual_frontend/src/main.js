import { createApp } from 'vue'
import './style.css'
import router from './router'
import store from './store'
import App from './App.vue'


import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faCircleCheck, faCircleExclamation, faTriangleExclamation, faMagnifyingGlass, faFileExcel, faBars, faFileCirclePlus, faBoxArchive, faCircleUser } from '@fortawesome/free-solid-svg-icons'

library.add(faCircleCheck, faCircleExclamation, faTriangleExclamation, faMagnifyingGlass, faFileExcel, faBars, faFileCirclePlus, faBoxArchive, faCircleUser )

const app = createApp(App)

app.use(router)
app.use(store)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
