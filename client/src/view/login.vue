<template>
<div>
<div class="login_blur"></div>
    <div class="login_style">
        <el-row class="login_style_blur">
            <el-col class="login-style">
                <p>点餐系统后台</p>
                <el-form :model="form" label-width="25px" ref="loginForm" :rules="rules" class="login">
                    <el-form-item prop="username">
                        <el-input v-model="form.username" placeholder="账号" :autofocus="true"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <input v-model="form.password" type="password" placeholder="密码" autocomplete="off" @keyup.enter="onSubmit('loginForm')" class="el-input__inner" />
                        <!-- <el-input v-model="form.password" type="password" placeholder="密码"></el-input> -->
                    </el-form-item>
                    <el-button type="primary" @click="onSubmit('loginForm')" class="login-button">登录</el-button>
                </el-form>
            </el-col>
        </el-row>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            login_url: '/api/admin/login',
            form: {
                username: '',
                password: ''
            },
            rules: {
                username: [
                    { required: true, message: '请输入账号', trigger: 'blur' }
                ],
                password: [
                    { required: true, message: '请输入密码', trigger: 'change' }
                ]
            }
        }
    },
    methods: {
        onSubmit(fromRef) {
            this.$refs[fromRef].validate(valid => {
                if (valid) {
                    this.$http.post(this.login_url, null, {
                        auth: this.form
                    }).then(res => {
                        if (res.data.status === 'ok') {
                            sessionStorage.setItem('is_login', true)
                            sessionStorage.setItem('user_name', res.data.user_name)
                            this.$router.push({
                                'path': '/admin/'
                            })
                        }
                    }).catch((error) => {
                        const errMsg = error.response.status === 500 ? '服务端发生异常' : '登陆失败请检查账号与密码'
                        this.$message({
                            showClose: true,
                            message: errMsg,
                            type: 'error'
                        })
                    })
                } else {
                    return false
                }
            })
        }
    },
    created() {
        const isLogin = sessionStorage.getItem('is_login') === 'true'
        const userName = sessionStorage.getItem('user_name')
        if (isLogin && userName) {
            this.$router.push({
                'path': '/admin/'
            })
        }
    }
}
</script>

<style scoped>
.login_blur {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
    background: url("../../static/images/bg.jpg") no-repeat top center;
    background-size: 100% 100%;
    background-attachment: fixed;
    z-index: 1;
}

.login_style {
    position: relative;
    width: 400px;
    margin-top: 340px;
    left: 50%;
    margin-left: -165px;
    /*border: 40px solid transparent;*/
    background: url("../../static/images/boxbg.png") no-repeat top center;
    background-size: cover;
    z-index: 3;
}
.login {
    width: 348px;
    padding-right: 30px;
    padding-bottom: 60px;
    padding-left: 15px;

}
.login-title-row {
    background-color: #5193e6;
    padding-left: 50px;
}
h1 {
    color: #FCFCFC;
    text-shadow: black 0.1em 0.1em 0.2em;
}
img {
    position: relative;
    transform: translate(-100%, 0);
    left: 95%;
}
.login-button {
    width: 322px;
    margin: 30px 0 0 25px;
    border: 0;
    background-color: #4a93e8;
}
p {
    text-align: center;
    width: 400px;
    padding: 30px 0 10px 0;
    margin-top: 0;
    color: #58a7e8;
    letter-spacing: 3px;
    font-size: 24px;
    font-family: "微软雅黑"
}
.el-input input {
        border: navajowhite;
}
</style>
