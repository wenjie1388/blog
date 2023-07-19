import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'


import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';
import './style.css';


const app = createApp(App)


// 全局注册 状态管理(store)
import { setupStore } from '@/stores';
setupStore(app);


// 全局挂载
app.use(ElementPlus);
app.use(createPinia())
app.use(router)

app.mount('#app')
