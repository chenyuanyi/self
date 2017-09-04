const webpack = require('webpack')
const baseConfig = require('./webpack.dll.user')
const userConfig = require('./config')
baseConfig.plugins.push(new webpack.HotModuleReplacementPlugin())
const proxyConf = {
}
if (userConfig.proxyUrlPath && userConfig.apiProxy) {
    proxyConf[userConfig.proxyUrlPath] = userConfig.apiProxy
}

baseConfig.devServer = {
    stats: 'errors-only',
    contentBase: baseConfig.output.path,
    publicPath: baseConfig.output.publicPath,
    hot: true,
    inline: true,
    historyApiFallback: true,
    port: userConfig.port,
    host: userConfig.host,
    proxy: proxyConf
}
module.exports = baseConfig
