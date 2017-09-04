<template>
    <el-row>
        <el-form :model="form" ref="form" :inline="true" :rules="rules">
            <el-form-item prop="username">
                <el-input placeholder="请输入用户名" v-model="form.username"></el-input>
            </el-form-item>
            <el-form-item prop="remark">
                <el-input placeholder="请输入真名" v-model="form.remark"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password" placeholder="请输入密码" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item prop="checkPassword">
                <el-input type="password" placeholder="请再次输入密码" v-model="form.checkPassword"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="addNewUser('form')">新建用户</el-button>
            </el-form-item>
        </el-form>
        <el-row>
            <el-table :data="userData">
                <el-table-column label="ID" prop="id"></el-table-column>
                <el-table-column label="用户名" prop="name"></el-table-column>
                <el-table-column label="真名" prop="remark"></el-table-column>
                <el-table-column label="操作">
                    <template scope="scope">
                        <el-button @click="changePermission(scope.row)">权限修改</el-button>
                        <el-button @click="changePwd(scope.row)">修改密码</el-button>
                        <el-button type="danger" @click="deleteUser(scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-row>
        <el-dialog :title="dialogTitle" v-model="dialogVisible" :close-on-click-modal="false">
            <el-tree
                ref="menu_tree"
                node-key="index"
                :data="menu"
                :props="defaultProps"
                show-checkbox>
            </el-tree>
            <el-row>
                <el-button type="primary" @click="savePermission">保存</el-button>
            </el-row>
        </el-dialog>
    </el-row>
</template>

<script>
    export default{
        data() {
            var passWordValid = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'))
                } else {
                    if (this.form.checkPassword !== '') {
                        this.$refs.form.validateField('checkPassword')
                    }
                    callback()
                }
            }
            var checkPassWordValid = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'))
                } else if (value !== this.form.password) {
                    callback(new Error('两次输入密码不一致!'))
                } else {
                    callback()
                }
            }
            return {
                userData: [],
                api_url: '/api/admin/system/user_manage',
                dialogVisible: false,
                dialogTitle: '',
                dialogUserId: 0,
                defaultProps: {
                    children: 'children',
                    label: 'name'
                },
                menu: [],
                form: {
                    username: '',
                    remark: '',
                    password: ''
                },
                rules: {
                    username: [{
                        required: true,
                        message: "请输入用户名",
                        trigger: 'blur'
                    }],
                    remark: [{
                        required: true,
                        message: "请输入真名",
                        trigger: 'blur'
                    }],
                    password: [{
                        validator: passWordValid,
                        trigger: 'blur'
                    }],
                    checkPassword: [{
                        validator: checkPassWordValid,
                        trigger: 'blur'
                    }]
                }
            }
        },
        methods: {
            getUserData: function () {
                this.$http.get(this.api_url).then(result => {
                    if (result.status === 200) {
                        this.userData = result.data
                    }
                })
            },
            getPermissionTree: function () {
                this.$http.get(this.api_url + '/get_permission').then(result => {
                    this.menu = result.data.menu_data
                }).catch(() => {
                    this.$message({
                        showClose: true,
                        message: '获取数据失败',
                        type: 'error'
                    })
                })
            },
            changePermission: function (row) {
                this.dialogTitle = '修改' + row.name + '的权限'
                this.dialogVisible = true
                this.dialogUserId = row.id
                this.$http.get(this.api_url + '/' + row.id).then(result => {
                    if (result.status === 200) {
                        if (result.data.menu) {
                            const menuTree = this.$refs['menu_tree']
                            const menuPermission = menuTree.getCheckedKeys()
                            menuPermission.forEach(val => {
                                menuTree.setChecked(val, false)
                            })
                            result.data.menu.forEach(val => {
                                menuTree.setChecked(val, true)
                            })
                        }
                    }
                }).catch(() => {
                    this.$message({
                        showClose: true,
                        message: "获取用户权限失败",
                        type: 'error'
                    })
                    this.dialogVisible = false
                })
            },
            savePermission: function () {
                const menuTreePermission = this.$refs['menu_tree'].getCheckedKeys()
                const permission = {
                    menu: menuTreePermission
                }
                const formData = {
                    'user_id': this.dialogUserId,
                    permission: permission,
                    flag: 'save_permission'
                }
                this.$http.post(this.api_url, formData).then(result => {
                    this.$message({
                        showClose: true,
                        message: result.data.msg
                    })
                    this.dialogVisible = false
                }).catch(() => {
                    this.$message({
                        showClose: true,
                        message: '保存权限失败!',
                        type: 'error'
                    })
                })
            },
            changePwd: function (row) {
                this.$prompt('请输入密码', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消'
                }).then(({
                             value
                         }) => {
                    const form_data = {
                        user_id: row.id,
                        new_password: value,
                        flag: 'change_password'
                    }
                    this.$http.post(this.api_url, form_data).then(result => {
                        this.$message({
                            type: 'success',
                            message: result.data.msg
                        })
                    })
                }).catch(() => {
                    this.$message({
                        type: 'error',
                        message: '未成功修改密码'
                    })
                })
            },
            deleteUser: function (row) {
                this.$confirm('此操作将永久删除该用户，是否继续？', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    const form_data = {
                        user_id: row.id,
                        flag: 'delete_user'
                    }
                    this.$http.post(this.api_url, form_data).then(result => {
                        let type = 'success'
                        if (result.data.state === 0) {
                            this.getUserData()
                        } else {
                            type = 'warning'
                        }
                        this.$message({
                            type: type,
                            message: result.data.msg
                        })
                    }).catch(() => {
                        this.$message({
                            type: 'error',
                            message: '未删除用户'
                        })
                    })
                })
            },
            addNewUser: function (formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        const form_data = {
                            name: this.form.username,
                            remark: this.form.remark,
                            password: this.form.password,
                            flag: 'create_user'
                        }
                        this.$http.post(this.api_url, form_data).then(result => {
                            if (result.data.state === 0) {
                                this.$refs[formName].resetFields()
                                this.getUserData()
                            }
                            this.$message({
                                type: 'success',
                                message: result.data.msg
                            })
                        }).catch(() => {
                            this.$message({
                                type: 'error',
                                message: '添加失败！'
                            })
                        })
                    }
                })
            }
        },
        created() {
            this.getUserData()
            this.getPermissionTree()
        }
    }
</script>

