<template>
<el-row>
    <el-col :span="12">
        <el-select v-model="AppId" placeholder="请选择应用" @change="getServerInfo">
            <el-option v-for='item in newAppInfo'
               :label="item.label"
               :value="item.value"
               :key="item.value">
            </el-option>
        </el-select>
    </el-col>
    <el-col :span="12" v-loading.body="ServerLoading">
        <el-select v-if="!multiple" v-model="ServerId" :filterable="filterable" placeholder="请选择区服" @change="updateValue">
            <el-option v-for='item in ServerInfo'
               :label="item.label"
               :value="item.value"
               :key="item.value">
            </el-option>
        </el-select>
        <zero-multiple-select
            ref="zero-multiple-select"
            v-model="ServerId"
            v-else
            :data="ServerInfo"
            node-key="value"
            :checkAll="true"
            @change="updateValue"
            :labelAll="serverLabel">
        </zero-multiple-select>
    </el-col>
</el-row>
</template>

<script>
import ZeroMultipleSelect from './zero_multiple_select'
export default {
    components: {
        ZeroMultipleSelect
    },
    props: {
        value: {
            required: true
        },
        AppInfo: {
            required: true,
            type: Array
        },
        multiple: {
            default: false,
            type: Boolean
        },
        filterable: {
            default: false,
            type: Boolean
        },
        autoCheck: {
            default: true,
            type: Boolean
        }
    },
    watch: {
        AppInfo(AppInfo_) {
            this.AppId = AppInfo_[0].value
            this.isFirst = true
        }
    },
    computed: {
        newAppInfo() {
            return this.AppInfo
        }
    },
    data() {
        return {
            ServerLoading: false,
            api_url: '/api/home/server_info',
            AppId: [],
            ServerId: this.multiple ? [] : null,
            ServerInfo: [],
            isFirst: false,
            nodeSelect: null,
            multipleOpen: false,
            serverLabel: '全选',
            serverIds: []
        }
    },
    methods: {
        getServerInfo() {
            if (this.AppId !== '' && this.AppId !== null) {
                this.ServerLoading = true
                const param_data = {
                    type: 'app_server',
                    app_id: this.AppId
                }
                return this.$http.post(this.api_url, param_data).then((res) => {
                    this.ServerInfo = []
                    this.ServerInfo = res.data.server_info

                    if (this.ServerInfo.length === 0) {
                        this.ServerId = ''
                        this.$alert("此应用无区服，请对此应用添加区服", "提示", {
                            confirmButtonText: '确定',
                            callback: action => {}
                        })
                        this.ServerLoading = false
                        return false
                    }
                    if (this.isFirst) {
                        this.isFirst = false
                        this.$nextTick(() => {
                            this.$emit('first-query')
                        })
                    }
                    this.ServerLoading = false
                }).catch(() => {
                    this.ServerLoading = false
                })
            }
        },
        updateValue(keys) {
            const value = keys || this.ServerId
            this.ServerId = value
            this.$emit('input', value)
            if (this.isFirst && !this.multiple && value) {
                this.isFirst = false
                this.$nextTick(() => {
                    this.$emit('first-query')
                })
            }
        },
        setAppInfo() {
            if (this.value.length > 0) {
                this.AppId = parseInt(this.value[0].split('_')[0])
            } else {
                this.AppId = this.AppInfo[0].value
            }
            this.getServerInfo().then(() => {
                this.ServerId = this.value
            })
        }
    },
    mounted() {
        if (this.newAppInfo.length > 0) {
            this.AppId = this.newAppInfo[0].value
        }
    }
}
</script>
<style>
.app-select-style {
    width: 100%
}
</style>
