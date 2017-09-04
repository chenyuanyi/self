const webpack = require('webpack')
const webpackDevServer = require('webpack-dev-server')
process.env.DEV = '1'
const config = require('./webpack.dll.user')
const userConfig = require('./config')
const listeningHost = "http://" + userConfig.host + ":" + userConfig.port
config.entry.dist.unshift("webpack-dev-server/client?" + listeningHost + "/", "webpack/hot/dev-server")
config.plugins.push(new webpack.HotModuleReplacementPlugin())
const proxyConf = {
}
if (userConfig.proxyUrlPath && userConfig.apiProxy) {
    proxyConf[userConfig.proxyUrlPath] = {
        target: userConfig.apiProxy
    }
}

const compiler = webpack(config)
compiler.plugin('done', (stats) => {
    console.log('!>watch')
    if (stats && stats.compilation && (stats.compilation.errors || stats.compilation.warnings) && (stats.compilation.errors.length > 0 || stats.compilation.warnings.length > 0)) {
        console.log(require('format-webpack-stats-errors-warnings')(stats, userConfig.projectPath))
    }
    console.log('!>compiler')
})

new webpackDevServer(compiler, {
    stats: 'errors-only',
    contentBase: config.output.path,
    publicPath: config.output.publicPath,
    hot: true,
    inline: true,
    quiet: true,
    historyApiFallback: true,
    proxy: proxyConf
}).listen(userConfig.port, userConfig.host, function(err, result) {
    if (err) {
        console.log(err)
    }
    console.log('Listening at ' + listeningHost)
})
