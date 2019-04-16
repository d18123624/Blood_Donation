import Vue from 'vue'
import Router from 'vue-router'

const Home = () => import('@/components/Home')
const SignIn = () => import('@/components/SignIn')
const SignUp = () => import('@/components/SignUp')
const Search = () => import('@/components/Search')
const Location = () => import('@/components/Location')
const PreviousSearches = () => import('@/components/PreviousSearches')
const IncomingRequests = () => import('@/components/IncomingRequests')

Vue.use(Router)

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            component: Home,
            name: 'Home',
            meta: {
                title: 'Home'
            }
        },
        {
            path: '/signup',
            component: SignUp,
            name: 'SignUp',
            meta: {
                title: 'Sign up'
            }
        },
        {
            path: '/signin',
            component: SignIn,
            name: 'SignIn',
            meta: {
                title: 'Sign In'
            }
        },
        {
            path: '/search',
            component: Search,
            name: 'Search',
            meta: {
                title: 'Search'
            }
        },
        {
            path: '/previoussearches',
            component: PreviousSearches,
            name: 'PreviousSearches',
            meta: {
                title: 'Previous searches'
            }
        },
        {
            path: '/incomingrequests',
            component: IncomingRequests,
            name: 'IncomingRequests',
            meta: {
                title: 'Incoming requests'
            }
        },
        {
            path: '/location/:lat/:lon',
            component: Location,
            name: 'Location',
            meta: {
                title: 'Location'
            }
        }
    ],
    /*scrollBehavior(to, from, savedPosition) {
        return { x: 0, y: 0 }
    }*/
})

router.beforeEach((to, from, next) => {
    // Update Meta Tags
    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title)
    const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags)

    if (nearestWithTitle) document.title = nearestWithTitle.meta.title

    Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el))

    if (!nearestWithMeta) return next()

    nearestWithMeta.meta.metaTags.map(tagDef => {
        const tag = document.createElement('meta')

        Object.keys(tagDef).forEach(key => {
            tag.setAttribute(key, tagDef[key])
        })

        // We use this to track which meta tags we create, so we don't interfere with other ones.
        tag.setAttribute('data-vue-router-controlled', '')

        return tag
    })
        .forEach(tag => document.head.appendChild(tag))

    next()
})

export default router
