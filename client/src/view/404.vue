<template lang="html">
  <h1>404</h1>
</template>

<script>
export default {
    beforeRouteEnter: (to, from, next) => {
        next(vm => {
            const indexVm = vm.$root.$children[0]
            indexVm.menuIndex = {}
            indexVm.breadcrumbData = [{ name: '404' }]
        })
    }
}
</script>

<style lang="css">
</style>
