export default [
    { path: "user_manage", component: resolve => require(['./sub_view/system/user_manage'], resolve) },
    { path: "*", component: resolve => require(["./404"], resolve) }
]
