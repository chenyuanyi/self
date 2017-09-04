const baseConfig = require('./webpack.base')
const path = require('path')
const webpack = require('webpack')

const vendors = [
    'vue',
    'axios',
    'vue-router',
    'element-ui',
    'element-ui/lib/theme-default/index.css',
    'es6-promise/auto',
    'vue-lazyload'
]
baseConfig.entry = {
    vendor: vendors
}
baseConfig.plugins.push(
    new webpack.DllPlugin({
        path: 'manifest.json',
        name: '[name]_[hash]',
        context: path.resolve(__dirname, '../')
    })
)
module.exports = baseConfig
