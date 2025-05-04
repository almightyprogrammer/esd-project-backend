import {createRouter, createWebHistory} from 'vue-router';
import Login from '../views/LoginPage.vue';
import AddNewItem from '../views/AddNewItemPage.vue';


const routes = [
    // Re-direct to the login url at the index url
    {
        path:'/',
        redirect: '/login'
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/club/items/new',
        name: 'AddNewItem',
        component: AddNewItem
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;