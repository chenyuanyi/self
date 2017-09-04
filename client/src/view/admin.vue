<template lang="html">
<div class="index_div">
    <el-row class="header">
        <el-col :span="5" :push="1">
            <h2 class="index_title">点餐系统</h2>
        </el-col>
        <el-col :span="6" :push="1">
        <el-menu class="top_menu" ref="top_menu" theme="dark" mode="horizontal" @select="TopMenuClick" :default-active="topDefaultIndex">
            <el-menu-item v-for="item in menu_data" :key="item.index" :index="item.index">{{item.name}}</el-menu-item>
        </el-menu>
        </el-col>
        <el-col :span="4" :push="10">
            <el-row>
                <el-col :span="11" class="user_login_out">
                    <h3>欢迎: {{userName}}</h3>
                </el-col>
                <el-col :span="4">
                    <el-button type="danger" class="user_login_out_button" @click="userLoginOut">退出</el-button>
                </el-col>
            </el-row>
        </el-col>
    </el-row>
    <el-row class="content">
        <el-col :span="3" :xs='8' class="left_menu">
            <div class="left_menu_row">
            <el-menu :router="true" ref="left_menu" :default-active="leftDefaultIndex" :unique-opened="true" @select="LeftMenuClick">
                <zero-tree-item v-for="item in sub_menu_data" :key="item.index" :tree_data="item">
                </zero-tree-item>
            </el-menu>
            </div>
        </el-col>
        <el-col :span="20" :xs="{span:16, push: 8}" :push="3" class="body_breadcrumb">
            <el-row class="breadcrumb_row">
                <el-breadcrumb separator="/" class="breadcrumb">
                  <el-breadcrumb-item :to="{ path: '/admin' }">首页</el-breadcrumb-item>
                  <el-breadcrumb-item v-for="bread in breadcrumbData" :key="bread.name">{{bread.name}}</el-breadcrumb-item>
                </el-breadcrumb>
            </el-row>
            <el-row class="sub_view">
                <router-view></router-view>
            </el-row>
        </el-col>
    </el-row>
</div>
</template>

<script>
import ZeroTreeItem from 'components/zero_tree_item'
export default {
    beforeRouteEnter: (to, from, next) => {
        if (sessionStorage.getItem('is_login') === 'true') {
            next()
        } else {
            next('/admin/login')
        }
    },
    data() {
        return {
            login_url: '/api/admin/login',
            menu_url: '/api/admin/menu',
            userName: '',
            menu_data: [],
            sub_menu_data: [],
            cacheTopIndex: '',
            topDefaultIndex: '',
            leftDefaultIndex: '',
            breadcrumbData: [{ name: '未选择' }]
        }
    },
    components: {
        ZeroTreeItem
    },
    methods: {
        TopMenuClick(index) {
            if (this.cacheTopIndex === index && this.sub_menu_data.length !== 0) {
                return
            }
            const clickMenu = this.menu_data.filter(k => {
                return k.index === index
            })
            if (clickMenu.length > 0 && clickMenu[0].children && clickMenu[0].children.length > 0) {
                this.sub_menu_data = clickMenu[0].children
                this.cacheTopIndex = index
                this.breadcrumbData = [
                    { name: '未选择' }
                ]
                this.$router.push({
                    path: '/admin'
                })
            }
        },
        leftMenuData(index) {
            if (this.cacheTopIndex === index && this.sub_menu_data.length !== 0) {
                return
            }
            const clickMenu = this.menu_data.filter(k => {
                return k.index === index
            })
            if (clickMenu.length > 0 && clickMenu[0].children && clickMenu[0].children.length > 0) {
                this.sub_menu_data = clickMenu[0].children
                this.cacheTopIndex = index
            }
        },
        LeftMenuClick(index, indexPath) {
            const meunData = this.allMenuData[index]
            this.setBreadcrumb(meunData.router_name || meunData.path)
        },
        setBreadcrumb(ortherTreeKey) {
            const treeKey = ortherTreeKey || this.$route.name || this.$route.path
            const treeMeunData = this.allPathMenuData[treeKey]
            const crumbData = []
            if (treeMeunData) {
                const topIndex = treeMeunData[0].index
                const leftIndex = treeMeunData[treeMeunData.length - 1].index

                this.$refs['top_menu'].activedIndex = topIndex
                this.$refs['left_menu'].activedIndex = leftIndex
                this.topDefaultIndex = topIndex
                this.leftDefaultIndex = leftIndex
                this.leftMenuData(topIndex)
                treeMeunData.forEach(val => {
                    if (val && val.name) {
                        crumbData.push({ name: val.name })
                    }
                })
                this.breadcrumbData = crumbData
            } else if (this.menu_data.length > 0) {
                const topIndex = this.menu_data[0].index
                this.leftMenuData(topIndex)
                this.$refs['top_menu'].activedIndex = topIndex
            }
        },
        userLoginOut() {
            this.$http.get(this.login_url).then(res => {
                sessionStorage.setItem('is_login', false)
                this.$router.push({
                    'path': '/admin/login'
                })
            })
        }
    },
    created() {
        this.$http.get(this.menu_url).then(res => {
            if (res.status === 200) {
                this.menu_data = res.data
                this.setBreadcrumb()
            }
        }).catch(() => {
            sessionStorage.setItem('is_login', false)
            this.$router.push({
                'path': '/admin'
            })
        })
        this.userName = sessionStorage.getItem('user_name')
    },
    watch: {
    },
    computed: {
        allMenuData() {
            const menuInfo = {}
            const initMeun = function(menuData) {
                menuData.forEach(val => {
                    const newVal = { name: val.name, path: val.path, router_name: val.router_name, index: val.index }
                    menuInfo[val.index] = newVal
                    if (val.children && val.children.length > 0) {
                        initMeun(val.children)
                    }
                })
            }
            initMeun(this.menu_data)
            return menuInfo
        },
        allPathMenuData() {
            const menuPathInfo = {}
            const initMeun = function(menuData, parent) {
                if (parent) {
                    parent = parent.concat()
                } else {
                    parent = []
                }
                menuData.forEach(val => {
                    const tmpParent = parent.concat()
                    parent.push({ name: val.name, path: val.path, router_name: val.router_name, index: val.index })
                    if (val.path || val.router_name) {
                        menuPathInfo[val.path || val.router_name] = parent
                    } else {
                        initMeun(val.children, parent)
                    }
                    parent = tmpParent
                })
            }
            initMeun(this.menu_data)
            return menuPathInfo
        }
    }
}
</script>

<style lang="css" scoped>
.index_div{
    padding-top: 4.3rem;
}
.header{
    background-color: #20a1ff;
    position: fixed;
    z-index: 2;
    height: 4.3rem;
    overflow: hidden;
    width: 100%;
    top: 0;
}
.left_menu{
    position: fixed;
    z-index: 2;
    height: 100%;
    left: 0;
    background-color: #eef1f6;
    padding-bottom: 4.3rem;
}
.left_menu_row{
    overflow-y: auto;
    height: 100%;
}
.body_breadcrumb{
    padding: 1.5rem;
    background-color: #FFF;
}
.sub_view{
    margin-top: 1.5rem;
    padding: 1.5rem;
    min-height: 40rem;
}
.index_title {
    color: #ffffff;
}
.user_login_out{
    color: #FFF;
}
.user_login_out_button{
    margin-top: 0.8rem;
}
.top_menu{
    background-color: #20a1ff;
}
.top_menu .el-menu-item{
  background-color: #20a1ff;
  color: #ffffff;
  font-size: 18px;
  /*font-weight: bold;*/
}
.top_menu .el-menu-item:hover{
  background-color: #20a1ff;
  color: #eef620;
}

.top_menu .is-active{
  color: #eef620
}

</style>
