/**
 * Created by Linjianhui on 2017/1/3.
 */
import 'es6-promise/auto'
import Vue from 'vue'
import Axios from 'axios'
import VueRouter from 'vue-router'
import ElementUi from 'element-ui'
import VueLazyload from 'vue-lazyload'
import 'element-ui/lib/theme-default/index.css'
import routerConfig from './config/router_config'
import './css/global.css'

Vue.use(VueRouter)
Vue.use(VueLazyload, {
    preLoad: 2,
    attempt: 1
})
ElementUi.install(Vue)
Vue.prototype.$http = Axios

Vue.prototype.$strftime = function (date, ftime, defkey) {
    const def = {
        all: '%Y-%m-%d %H:%M:%S',
        day: '%Y-%m-%d',
        time: '%H:%M:%S'
    }
    ftime = ftime || def[defkey] || def['all']
    return ftime.replace(/%\w/g, function (match) {
        switch (match) {
        case '%Y':
            return date.getFullYear()
        case '%m':
            return date.getMonth() + 1
        case '%d':
            return date.getDate()
        case '%H':
            return date.getHours()
        case '%M':
            return date.getMinutes()
        case '%S':
            return date.getSeconds()
        default:
            return match
        }
    })
}

Vue.mixin({
    methods: {
        handleRangeDatetime(datetime, format_type) {
            if (datetime && datetime.length > 0) {
                datetime = datetime.map(i => new Date(i)).map(i => this.$strftime(i, '', format_type))
                if (datetime[0].indexOf('1970') > -1) {
                    datetime = []
                }
            } else {
                datetime = []
            }
            return datetime
        }
    }
})

const router = new VueRouter({
    mode: 'history',    // 路由的模式
    routes: routerConfig
})
new Vue({
    el: '#root',
    router,
    render: h => h("router-view")
})
