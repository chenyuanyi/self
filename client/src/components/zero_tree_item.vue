<template lang="html">
    <el-submenu v-if="is_submenu" :index="tree_data.index">
        <template slot="title">{{tree_data.name}}</template>
        <zero-tree-item v-for="item in tree_data.children" :key="item.index" :tree_data="item" :count="count + 1">
        </zero-tree-item>
    </el-submenu>
    <el-menu-item-group v-else-if="is_group" :title="tree_data.name">
        <zero-tree-item v-for="item in tree_data.children" :key="item.index" :tree_data="item" :count="count + 1">
        </zero-tree-item>
    </el-menu-item-group>
    <el-menu-item v-else :index="tree_data.index" :route="itemRoute">{{tree_data.name}}</el-menu-item>
</template>

<script>
export default {
    name: "zero-tree-item",
    computed: {
        is_submenu() {
            return this.tree_data.children && this.tree_data.children.length && !this.tree_data.path && this.count < 1
        },
        is_group() {
            return this.count > 0 && this.tree_data.children && this.tree_data.children.length
        },
        itemRoute() {
            const RouteObj = {}
            if (this.tree_data.path) {
                RouteObj.path = this.tree_data.path
            } else if (this.tree_data.router_name) {
                RouteObj.name = this.tree_data.router_name
            }
            return RouteObj
        }
    },
    props: {
        tree_data: {
            type: Object
        },
        count: {
            type: Number,
            default: 0
        }
    }
}
</script>
