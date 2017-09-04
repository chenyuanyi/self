/**
 * Created by linjianhui on 2017/1/4.
 */
import MenuConfig from "../view/menu_config"
export default [
    { path: "/admin/login", component: resolve => require(["../view/login"], resolve) },
    {
        path: "/admin",
        component: resolve => require(["../view/admin"], resolve),
        children: MenuConfig
    },
    { path: "*", component: resolve => require(["../view/404"], resolve) }
]
