<template lang="html">
<div class="color-list">
    <el-card :body-style="{ padding: '0px' }" v-for="color in colors" v-dragging="{ item: color, list: colors, group: 'color' }" :key="color.text" class="item">
      <div style="padding: 14px;">
        <span>{{ color.text }}</span>
        <div class="bottom clearfix">
          <time class="time">{{ color.text }}</time>
          <el-button type="text" class="button">操作按钮</el-button>
        </div>
      </div>
    </el-card>
</div>
</template>

<script>
export default {
    data () {
        return {
            colors: [{
                text: "Aquamarine",
                orders: 1
            }, {
                text: "Hotpink",
                orders: 2
            }, {
                text: "Gold",
                orders: 3
            }]
        }
    },
    beforeRouteEnter: (to, from, next) => {
        next(vm => {
            const indexVm = vm.$root.$children[0]
            indexVm.menuIndex = {}
            indexVm.breadcrumbData = [{ name: '404' }]
        })
    },
    mounted() {
        this.$dragging.$on('dragged', (res) => {
            console.log(res.draged.orders, res.draged.text)
            console.log(res.to.orders, res.to.text)
        })
        this.$dragging.$on('dragend', () => {
            console.log('end')
        })
    }
}
</script>

<style lang="css">
.item{
    width: 10rem;
    height: 10rem;
    float: left;
    background: #f5f5f5;
    padding: .5rem;
    color: #5f5f5f;
    transition: transform .3s;
}
.image {
    width: 10%;
    display: block;
  }
</style>
