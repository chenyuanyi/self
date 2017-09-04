<template>
<div ref="select-multiple" class="select-multiple">
    <el-input
        @click.native="openSelect"
        v-model="jsonValue"
        :readonly="true"
        placeholder="请选择"
        :icon="multipleOpen ? 'caret-top': 'caret-bottom'">
    </el-input>
    <div class="select-multiple-tree" v-show="multipleOpen">
        <zero-tree ref="select-multiple-tree"
            :treeData="newData"
            v-model="newValue"
            :options="options"
            @handleCheckedChange="handleCheckedChange"
            style="width: 300px;"
        />
    </div>
</div>
</template>
<script>
export default {
    name: 'zero-multiple-select',
    props: {
        value: {
            type: Array,
            required: true
        },
        data: {
            type: Array,
            required: true
        },
        checkAll: {
            type: Boolean,
            default: true
        },
        checkAllKey: {
            type: Number,
            default: -1
        },
        label: {
            type: String,
            default: () => 'label'
        },
        children: {
            type: String,
            default: 'children'
        },
        nodeKey: {
            type: String,
            default: 'id'
        },
        defaultAll: {
            type: Boolean,
            default: true
        },
        labelAll: {
            type: String,
            default: '所有'
        }
    },
    watch: {
        value(newVal) {
            if (this.propChange) {
                this.newValue = newVal
                this.$nextTick(() => {
                    this.Labels = this.$refs['select-multiple-tree'].getCheckLabels()
                })
            } else {
                this.propChange = true
            }
        },
        data(newVal) {
            this.newData = this.checkAll ? [{ [this.nodeKey]: this.checkAllKey, open: true, [this.label]: '全选', [this.children]: newVal.slice(0) }] : newVal.slice(0)
        }
    },
    mounted() {
        this.documentClick = (e) => {
            if (!this.$el.contains(e.target)) {
                document.removeEventListener('click', this.documentClick)
                this.multipleOpen = false
            }
        }
    },
    beforeDestroy() {
        document.removeEventListener('click', this.documentClick)
    },
    data() {
        return {
            Labels: [],
            multipleOpen: false,
            newValue: [],
            propChange: true,
            options: { treeKey: this.nodeKey, children: this.children, label: this.label, showCheckbox: true },
            newData: this.checkAll ? [{ [this.nodeKey]: this.checkAllKey, open: true, [this.label]: '全选', [this.children]: this.data.slice(0) }] : this.data.slice(0)
        }
    },
    computed: {
        jsonValue() {
            return this.Labels.length > 0 ? JSON.stringify(this.Labels) : ''
        }
    },
    methods: {
        // setServerInfo() {
        // },
        openSelect() {
            this.multipleOpen = !this.multipleOpen
            if (this.multipleOpen) {
                this.$nextTick(() => {
                    document.addEventListener('click', this.documentClick)
                })
            } else {
                this.$nextTick(() => {
                    document.removeEventListener('click', this.documentClick)
                })
            }
        },
        handleCheckedChange() {
            this.propChange = false
            this.$emit('input', this.newValue)
            this.$emit('change')
            this.Labels = this.$refs['select-multiple-tree'].getCheckLabels()
        },
        treeCheckAll() {
            this.$refs['select-multiple-tree'].checkAll(true)
        }
    }
}
</script>

<style>
.select-multiple {
    position:relative;
    width:100%;
}
.select-multiple-tree {
    border: 1px solid #20a1ff;
    width:100%;
    position:absolute;
    z-index:200;
    max-height:300px;
    overflow:auto;
    background-color: #fff;
    max-width: 300px;
}
</style>
